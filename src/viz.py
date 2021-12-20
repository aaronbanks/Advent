from itertools import chain
from dataclasses import dataclass, astuple as as_tuple
from abc import ABC, abstractmethod
from random import random

import tkinter as tk
from tkinter import ttk
from typing import Iterable, List, Optional

from PIL import Image, ImageTk, ImageDraw

# Minimum and maximum pixel dimensions for the generated image.
MAX_SIZE = 720
MIN_SIZE = 180


@dataclass(frozen=True)
class Transformation:
    x_scale: float = 1.0
    y_scale: float = 1.0
    x_offset: float = 0.0
    y_offset: float = 0.0

    def __call__(self, point: "Point") -> "Point":
        return Point(
            point.x * self.x_scale + self.x_offset,
            point.y * self.y_scale + self.y_offset,
        )


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Bounds:
    min: Point
    max: Point

    def padded(self, padding: float) -> "Bounds":
        return Bounds(
            Point(self.min.x - padding, self.min.y - padding),
            Point(self.max.x + padding, self.max.y + padding),
        )


@dataclass(frozen=True)
class AbstractGraphic(ABC):
    @abstractmethod
    def points(self) -> Iterable[Point]:
        return []


@dataclass(frozen=True)
class ArrowGraphic(AbstractGraphic):
    source: Point
    target: Point

    def points(self):
        yield self.source
        yield self.target


@dataclass(frozen=True)
class PathGraphic(AbstractGraphic):
    path_points: List[Point]

    def points(self):
        yield from self.path_points


@dataclass(frozen=True)
class DotGraphic(AbstractGraphic):
    center: Point

    def points(self):
        yield self.center


class Visualization:
    def __init__(self):
        self.x: float = 0
        self.y: float = 0
        self.graphics: List[AbstractGraphic] = []
        self.current_path: Optional[PathGraphic] = None

    def move_to(self, x, y):
        """Moves the pen to the coordinates, without drawing anything."""
        self.x = x
        self.y = y
        self.current_path = None

    def line_to(self, x, y=None):
        """Moves the pen to the coordinates, stroking a line along the way."""
        if y is None:
            y = self.y + 1

        if self.current_path is None:
            self.current_path = PathGraphic([Point(self.x, self.y)])
            self.graphics.append(self.current_path)
        self.current_path.path_points.append(Point(x, y))
        self.x = x
        self.y = y

    def point_at(self, x, y):
        """Draws an arrow from the pen to the coordinates, without moving the pen."""
        self.graphics.append(
            ArrowGraphic(
                source=Point(self.x, self.y),
                target=Point(x, y),
            )
        )

    def dot_at(self, x, y):
        """Draws a dot at the coordinates, without moving the pen."""
        self.graphics.append(DotGraphic(Point(x, y)))

    def points(self) -> Iterable[Point]:
        for graphic in self.graphics:
            yield from graphic.points()

    def bounds(self) -> Bounds:
        count = 0

        for point in self.points():
            if count == 0 or point.x < x_min:
                x_min = point.x
            if count == 0 or point.y < y_min:
                y_min = point.y
            if count == 0 or point.x > x_max:
                x_max = point.x
            if count == 0 or point.y > y_max:
                y_max = point.y

            count += 1

        if count >= 2:
            return Bounds(
                Point(x_min, y_min),
                Point(x_max, y_max),
            )
        elif count == 1:
            return Bounds(
                Point(x_min - 1, y_min - 1),
                Point(x_max + 1, y_max + 1),
            )
        else:
            return Bounds(Point(0, 0), Point(1, 1))

    def render(self):
        bounds = self.bounds()
        print(f"[viz] Inner bounds: {bounds}")

        bounds = bounds.padded(2)
        bounds_width = bounds.max.x - bounds.min.x
        bounds_height = bounds.max.y - bounds.min.y

        if bounds_width > bounds_height:
            scale = MAX_SIZE / bounds_width
        else:
            scale = MAX_SIZE / bounds_height

        to_pixel_space = Transformation(
            scale, scale, -bounds.min.x * scale, -bounds.min.y * scale
        )

        print(f"[viz] to_pixel_space: {to_pixel_space}")

        outer_width = int(clamp(MIN_SIZE, scale * bounds_width, MAX_SIZE))
        outer_height = int(clamp(MIN_SIZE, scale * bounds_height, MAX_SIZE))

        image = Image.new(
            mode="RGBA",
            size=(outer_width, outer_height),
            color=(0x00, 0x00, 0x00, 0xFF),
        )

        def alpha_draw(f):
            buffer = Image.new(
                mode="RGBA",
                size=image.size,
                color=(0x00, 0x00, 0x00, 0x00),
            )

            buffer_draw = ImageDraw.Draw(buffer)

            f(buffer_draw)

            image.alpha_composite(buffer)

        line_color_index = 0
        line_colors = [
            (0xFF, 0xFF, 0xFF, 0xE0),
            (0x80, 0xFF, 0xD0, 0xE0),
            (0xD0, 0x80, 0xFF, 0xE0),
            (0x80, 0xD0, 0xFF, 0xE0),
        ]

        for graphic in self.graphics:
            if isinstance(graphic, PathGraphic):
                width = int(clamp(1, scale * 0.125, 16))

                alpha_draw(
                    lambda draw: draw.line(
                        [as_tuple(to_pixel_space(point)) for point in graphic.points()],
                        fill=line_colors[line_color_index % len(line_colors)],
                        width=width,
                        joint="curve",
                    )
                )

                line_color_index += 1
            elif isinstance(graphic, ArrowGraphic):
                width = int(clamp(1, scale * 0.125, 16))

                @alpha_draw
                def _(draw):
                    for (dx, dy) in (
                        (-0.125, 0),
                        (+0.125, 0),
                        (0, 0.125),
                        (0, -0.125),
                        (0, 0),
                    ):
                        t = Transformation(1, 1, dx, dy)
                        source = as_tuple(to_pixel_space(t(graphic.source)))
                        target = as_tuple(to_pixel_space(graphic.target))
                        draw.line(
                            [source, target],
                            fill=(0x80, 0xD0, 0xFF, 0x40),
                            width=width,
                        )

            elif isinstance(graphic, DotGraphic):
                center = to_pixel_space(graphic.center)

                dot_radius = clamp(2, scale * 0.5, 32)
                alpha_draw(
                    lambda draw: draw.ellipse(
                        [
                            center.x - dot_radius,
                            center.y - dot_radius,
                            center.x + dot_radius,
                            center.y + dot_radius,
                        ],
                        fill=(0xFF, 0xD0, 0x00, 0xD0),
                    )
                )
            else:
                raise TypeError(f"expected a *Graphic, but got this: {graphic!r}")

        return image

    def show(self):
        """Opens a window to display the current state of the visualization.

        This blocks the script until the window is closed.
        """

        image = self.render()

        root = tk.Tk()
        root.title("Advent of Code")
        root.resizable(False, False)

        tk_image = ImageTk.PhotoImage(image)
        panel = ttk.Label(root, image=tk_image)
        panel.pack(fill="both", expand="yes")

        close_button = ttk.Button(root, text="Close", command=root.destroy)
        close_button.pack(fill="both", expand="yes")
        close_button.focus_set()

        root.focus_force()
        root.mainloop()


def clamp(min, x, max):
    if x < min:
        return min
    elif x > max:
        return max
    else:
        return x


# A default instance, with methods exported as module functions, for ease of use.
_default = Visualization()
move_to = _default.move_to
line_to = _default.line_to
point_at = _default.point_at
dot_at = _default.dot_at
show = _default.show


def main():
    move_to(10, 10)
    line_to(20, 20)
    point_at(10, 20)
    dot_at(20, 10)
    show()


if __name__ == "__main__":
    main()

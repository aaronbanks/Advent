from itertools import chain
from dataclasses import dataclass
from abc import ABC, abstractmethod

import tkinter as tk
from tkinter import ttk
from typing import Iterable, List, Optional

from PIL import Image, ImageTk

# import aggdraw

# Minimum and maximum pixel dimensions for the generated image.
MAX_SIZE = 720
MIN_SIZE = 180

# LINE_PEN = aggdraw.Pen(
#     color=(0xFF, 0xFF, 0xFF),
#     width=4,
# )
#
# ARROW_PEN = aggdraw.Pen(
#     color=(0x80, 0xC0, 0xFF, 0x80),
#     width=1,
# )


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Bounds:
    min: Point
    max: Point


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

    def line_to(self, x, y):
        """Moves the pen to the coordinates, stroking a line along the way."""
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
        x_min = 0
        y_min = 0
        x_max = 1
        y_max = 1

        for point in self.points():
            if point.x < x_min:
                x_min = point.x
            if point.y < y_min:
                y_min = point.y
            if point.x > x_max:
                x_max = point.x
            if point.y > y_max:
                y_max = point.y

        return Bounds(
            Point(x_min, y_min),
            Point(x_max, y_max),
        )

    def render(self):
        bounds = self.bounds()
        bounds_width = bounds.max.x - bounds.min.x
        bounds_height = bounds.max.y - bounds.min.y

        if bounds_width > bounds_height:
            inner_scale = MAX_SIZE / bounds_width
        else:
            inner_scale = MAX_SIZE / bounds_height

        inner_x_offset = -bounds.min.x
        inner_y_offset = -bounds.min.y

        outer_width = min(MAX_SIZE, max(MIN_SIZE, inner_scale * bounds_width))
        outer_height = min(MAX_SIZE, max(MIN_SIZE, inner_scale * bounds_height))

        image = Image.new(
            mode="RGBA",
            size=(outer_width, outer_height),
            color=(0x00, 0x00, 0x00, 0xFF),
        )

        draw = aggdraw.Draw(image)

        for graphic in self.graphics:
            if isinstance(graphic, PathGraphic):
                draw.line(
                    [
                        c
                        for point in graphic.points()
                        for c in (
                            inner_scale * (inner_x_offset + point.x),
                            inner_scale * (inner_y_offset + point.y),
                        )
                    ],
                    LINE_PEN,
                )
            elif isinstance(graphic, ArrowGraphic):
                draw.line(
                    [
                        c
                        for point in graphic.points()
                        for c in (
                            inner_scale * (inner_x_offset + point.x),
                            inner_scale * (inner_y_offset + point.y),
                        )
                    ],
                    ARROW_PEN,
                )
            else:
                raise TypeError(f"expected a *Graphic, but got this: {graphic!r}")

        draw.flush()

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

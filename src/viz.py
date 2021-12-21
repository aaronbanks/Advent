import sys
from itertools import cycle
from dataclasses import dataclass, astuple as as_tuple, field
from abc import ABC, abstractmethod

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile as ask_save_as_file
from typing import Any, Iterable, List, Optional

from PIL import Image, ImageTk, ImageDraw

# Minimum and maximum pixel dimensions for the generated image.
MAX_SIZE = 720
MIN_SIZE = 90

default_line_colors = iter(
    cycle(
        [
            (0x80, 0xFF, 0xD0, 0xFF),
            (0xD0, 0x80, 0xFF, 0xFF),
            (0x80, 0xD0, 0xFF, 0xFF),
        ]
    )
)

default_arrow_colors = iter(
    cycle(
        [
            (0x80, 0xFF, 0xD0, 0x80),
            (0xD0, 0x80, 0xFF, 0x80),
            (0x80, 0xD0, 0xFF, 0x80),
        ]
    )
)

default_dot_colors = iter(
    cycle(
        [
            (0xC0, 0xFF, 0xE0, 0xFF),
            (0xE0, 0xC0, 0xFF, 0xFF),
            (0xC0, 0xE0, 0xFF, 0xFF),
        ]
    )
)


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


@dataclass
class AbstractGraphic(ABC):
    color: any
    z: float

    @abstractmethod
    def points(self) -> Iterable[Point]:
        return []


@dataclass
class ArrowGraphic(AbstractGraphic):
    source: Point
    target: Point

    def points(self):
        yield self.source
        yield self.target


@dataclass
class PathGraphic(AbstractGraphic):
    path_points: List[Point]

    def points(self):
        yield from self.path_points


@dataclass
class DotGraphic(AbstractGraphic):
    center: Point

    def points(self):
        yield self.center


@dataclass
class Layer:
    viz: "Visualization"

    line_color: Any
    arrow_color: Any
    dot_color: Any

    x: float = 0
    y: float = 0
    z: float = 0
    current_path: Optional[PathGraphic] = None

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
            self.current_path = PathGraphic(
                color=self.line_color,
                z=self.z,
                path_points=[Point(self.x, self.y)],
            )
            self.viz.graphics.append(self.current_path)
        self.current_path.path_points.append(Point(x, y))
        self.x = x
        self.y = y

    def point_at(self, x, y):
        """Draws an arrow from the pen to the coordinates, without moving the pen."""
        self.viz.graphics.append(
            ArrowGraphic(
                color=self.arrow_color,
                z=self.z,
                source=Point(self.x, self.y),
                target=Point(x, y),
            )
        )

    def dot_at(self, x, y):
        """Draws a dot at the coordinates, without moving the pen."""
        self.viz.graphics.append(
            DotGraphic(color=self.dot_color, z=self.z, center=Point(x, y))
        )


@dataclass
class Visualization:
    graphics: List[AbstractGraphic] = field(default_factory=list)
    _default_layer: Optional["Layer"] = None

    def default_layer(self):
        if self._default_layer is None:
            self._default_layer = self.new_layer()
        return self._default_layer

    def new_layer(
        self, color=None, line_color=None, arrow_color=None, dot_color=None, z=0
    ):
        return Layer(
            self,
            line_color=line_color or color or next(default_line_colors),
            arrow_color=arrow_color or color or next(default_arrow_colors),
            dot_color=dot_color or color or next(default_dot_colors),
            z=z,
        )

    def move_to(self, x, y):
        """Moves the pen to the coordinates, without drawing anything."""
        self.default_layer().move_to(x, y)

    def line_to(self, x, y=None):
        """Moves the pen to the coordinates, stroking a line along the way."""
        self.default_layer().line_to(x, y)

    def point_at(self, x, y):
        """Draws an arrow from the pen to the coordinates, without moving the pen."""
        self.default_layer().point_at(x, y)

    def dot_at(self, x, y):
        """Draws a dot at the coordinates, without moving the pen."""
        self.default_layer().dot_at(x, y)

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

    def render(self, oversample=1):
        bounds = self.bounds()

        bounds = bounds.padded(2)
        bounds_width = bounds.max.x - bounds.min.x
        bounds_height = bounds.max.y - bounds.min.y

        if bounds_width > bounds_height:
            scale = int(MAX_SIZE * oversample) / bounds_width
        else:
            scale = int(MAX_SIZE * oversample) / bounds_height

        to_pixel_space = Transformation(
            scale, scale, -bounds.min.x * scale, -bounds.min.y * scale
        )

        outer_width = int(scale * bounds_width)
        outer_height = int(scale * bounds_height)

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

        for graphic in sorted(self.graphics, key=lambda g: g.z):
            if isinstance(graphic, PathGraphic):
                width = int(clamp(1, scale * 0.25, 16))

                alpha_draw(
                    lambda draw: draw.line(
                        [as_tuple(to_pixel_space(point)) for point in graphic.points()],
                        fill=graphic.color,
                        width=width,
                        joint="curve",
                    )
                )
            elif isinstance(graphic, ArrowGraphic):
                width = int(clamp(1, scale * 0.125, 16))

                @alpha_draw
                def _(draw):
                    source = as_tuple(to_pixel_space(graphic.source))
                    target = as_tuple(to_pixel_space(graphic.target))
                    draw.line(
                        [source, target],
                        fill=graphic.color,
                        width=width,
                    )

            elif isinstance(graphic, DotGraphic):
                center = to_pixel_space(graphic.center)

                dot_radius = clamp(2, scale * 0.4, 32)
                alpha_draw(
                    lambda draw: draw.ellipse(
                        [
                            center.x - dot_radius,
                            center.y - dot_radius,
                            center.x + dot_radius,
                            center.y + dot_radius,
                        ],
                        fill=graphic.color,
                    )
                )
            else:
                raise TypeError(f"expected a *Graphic, but got this: {graphic!r}")

        return image

    def show(self, oversample=4):
        """Opens a window to display the current state of the visualization.

        This blocks the script until the window is closed.
        """

        image = self.render(oversample=oversample)

        root = tk.Tk()
        root.title(f"Visualization - {sys.argv[0]}")
        root.resizable(False, False)

        scaled_image = image.resize(
            (
                int(image.width / oversample),
                int(image.height / oversample),
            ),
            Image.BICUBIC,
        )
        tk_image = ImageTk.PhotoImage(scaled_image)
        panel = ttk.Label(root, image=tk_image)
        panel.pack(fill="both", expand="yes")

        def save_as():
            target_file = ask_save_as_file(
                defaultextension="png",
                mode="wb",
                filetypes=[("PNG Image", "*.png")],
                title="Save Visualization As…",
            )
            if target_file is not None:
                scaled_image.save(target_file)

        save_button = ttk.Button(root, text="Save As…", command=save_as)
        save_button.pack(fill="both", expand="yes", ipady=4)
        save_button.focus_set()

        close_button = ttk.Button(root, text="Close", command=root.destroy)
        close_button.pack(fill="both", expand="yes", ipady=4)
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
new_layer = _default.new_layer


def main():
    move_to(10, 10)
    line_to(20, 20)
    point_at(10, 20)
    dot_at(20, 10)
    show()


if __name__ == "__main__":
    main()

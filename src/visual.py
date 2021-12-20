from itertools import chain
from dataclasses import dataclass
from os import startfile

import tkinter as tk
from tkinter import ttk
from typing import Iterable, Iterator

from PIL import Image, ImageTk
import aggdraw


"""
What capabilities?

We want to display dots in cells?


"""

@dataclass(frozen=True)
class Point:
    x: float
    y: float

@dataclass(frozen=True)
class Bounds:
    min: Point
    max: Point

@dataclass(frozen=True)
class Graphic:
    def points(self) -> Iterable[Point]:
        return []

    def bounds(self) -> Bounds:
        x_min = -1
        y_min = -1
        x_max = +1
        y_max = +1

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




@dataclass(frozen=True)
class Arrow(Graphic):
    start: Point
    end: Point

    def __iter__(self):
        yield self.start
        yield self.end

@dataclass(frozen=True)
class Path(Graphic):
    points: Point

@dataclass(frozen=True)
class Dot(Graphic):
    center: Point




class Visualization:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.graphics = []

    def move_to(self, x, y):
        """Moves the pen to the coordinates, without drawing anything."""
        self.x = x
        self.y = y
        self.coords.extend([(self.x, self.y)])

    def stroke_to(self, x, y):
        """Moves the pen to the coordinates, stroking a line along the way."""
        self.x = x
        self.y = y
        self.coords.extend([(self.x, self.y)])

    def peek_at(self, x, y):
        """Draws a line from the pen to the coordinates, without moving the pen."""
        self.coords.extend([(x, y), (self.x, self.y)])

    def dot_at(self, x, y):
        """Draws a dot at the coordinates, without moving the pen."""
        self.coords.extend([(x, y), (self.x, self.y)])

    def render(self):
        image = Image.new(
            mode="RGB",
            size=(512, 512),
            color=(0, 0, 0),
        )

        draw = aggdraw.Draw(image)
        pen = aggdraw.Pen(
            color=(0xFF, 0xFF, 0xFF),
            width=2,
        )

        coords = list(chain.from_iterable(self.coords))
        coords = [c * 20 + 200 for c in coords]

        draw.line(
            coords,
            pen,
        )
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


def main():
    viz = Visualization()

    viz.show()
    viz.show()


if __name__ == "__main__":
    main()

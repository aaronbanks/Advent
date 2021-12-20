from itertools import chain

import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageShow, ImageTk
import aggdraw


"""
What capabilities?

We want to display dots in cells?


"""


class Visualization:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.coords = []

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

        coords = list(chain(*self.coords))
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

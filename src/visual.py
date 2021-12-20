import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageShow, ImageTk
import aggdraw


class InfiniteCanvas:
    def __init__(self):
        self.default_line = CanvasLine(self)

    def line(self, x: float, y: float):
        self.default_line.line(x, y)

    def show(self):
        image = self.render()
        ImageShow.show(image)


class CanvasLine:
    def __init__(self, canvas: InfiniteCanvas):
        self.canvas = canvas

    def line(self, x: float, y: float):
        pass


def main():
    image = Image.new(
        mode="RGB",
        size=(512, 512),
        color=(0, 0, 0),
    )

    draw = aggdraw.Draw(image)
    pen = aggdraw.Pen(
        color=(0xFF, 0xFF, 0xFF),
        width=4,
    )
    draw.line(
        [
            0,
            0,
            64,
            64,
            100,
            50,
            50,
            100,
            0,
            0,
        ],
        pen,
    )
    draw.flush()

    root = tk.Tk()
    root.title("Advent of Code")
    root.resizable(False, False)

    tk_image = ImageTk.PhotoImage(image)
    panel = tk.Label(root, image=tk_image)
    panel.pack(fill="both", expand="yes")

    root.mainloop()


if __name__ == "__main__":
    main()

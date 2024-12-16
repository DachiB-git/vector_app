from tkinter import *

BACKGROUND_COLOR = "gray"


class Window:
    root = None

    def __init__(self, title, width, height):
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title(title)
        self.root.configure(background=BACKGROUND_COLOR)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

    def get_root(self):
        return self.root

    def run(self):
        self.root.mainloop()


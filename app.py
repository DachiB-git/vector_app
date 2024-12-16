from stock import Stock
from window import Window

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480


class App(Window):
    windows = []

    def __init__(self, title, width, height):
        stock = Stock()
        super().__init__(title, width, height)

    def add_new_window(self, title):
        window = Window(title, WINDOW_WIDTH, WINDOW_HEIGHT)
        window.run()
        self.windows.append(window)

    # def bind_window(self, window):
    #     self.stock.bind(window)

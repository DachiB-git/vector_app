import csv
from iitem import StockItem
from pathlib import Path
from state import State


class Stock(State):
    stock_items = {}

    def __init__(self):
        self.load_stock()

    def load_stock(self):
        stock_file = Path("stock.csv")
        if stock_file.is_file():
            with open(stock_file, encoding="UTF-8") as stock_file:
                reader = csv.reader(stock_file)
                for row in reader:
                    item_id = row[0]
                    stock_item = StockItem(*row)
                    self.stock_items[item_id] = stock_item
        for k,v in self.stock_items.items():
            print(v)

    def bind_observer(self, observer):
        self.observers.append(observer)

    def get_state(self):
        return self.stock_items

    def set_state(self, stock_items):
        self.stock_items = stock_items
        self.notify()

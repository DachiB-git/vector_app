# # Import the required Libraries
# from tkinter import *
# from tkinter import ttk
# import tkinter as tk
# import csv
# from iitem import StockItem
# from app import App
# from zeep import Client
#
#
# def load_stock(file_name):
#     return open(file_name, encoding="UTF-8")
#
#
# def update_stock_list():
#     with load_stock("stock.csv") as stock_file:
#         reader = csv.reader(stock_file)
#         for row in reader:
#             mylist.insert(tk.END, f"{row[1]}  {row[3]}")
#
#
# def toggle_list_visibility():
#     if mylist.winfo_ismapped():
#         mylist.grid_forget()  # Hide the list
#     else:
#         mylist.grid(padx=0, pady=0)  # Show the list
#
#
# def parse_good(good):
#     return [good[i].text for i in range(len(good))]
#
#
#
#
# imported_waybills = []
# csv_header = ['საქონლის კოდი', 'საქონლის დასახელება', 'ზომის ერთეული', 'რაოდენობა', "ერთ.ფასი", "საქონლის ფასი",
#               "დაბეგვრა"]
# # Create an instance of Tkinter frame
# win = Tk()
#
# # Set the geometry of Tkinter frame
# win.geometry("2000x1000")
# win.title("Vector")
# win.configure(background="#A6F0F1")
#
#
# def do():
#     global entry, global_stock, stock, csv_header
#     waybill_number = entry.get()
#     imported_waybills.append(waybill_number)
#     stock = {}
#     rs_wsdl = "https://services.rs.ge/WayBillService/WayBillService.asmx?WSDL"
#     client = Client(wsdl=rs_wsdl)
#     password = "123456"
#     # su = "YVELAMGAMOIYENET12:206322102"
#     # sp = password
#     su = "AGRO:406253138"
#     sp = "agro123"
#     waybill = client.service.get_waybill_by_number(su, sp, waybill_number)
#     goods = waybill[1]
#
#     for good in goods:
#         params = parse_good(good)
#         good_id = params[0]
#         obj = StockItem(*params)
#         stock[good_id] = obj
#         global_stock[good_id] = obj
#
#         label.configure(text="imported successfully")
#     update_stock_list()
#
#     with open('export.csv', 'w', newline='', encoding="UTF-8") as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(csv_header)
#         for k, item in stock.items():
#             writer.writerow(item.to_list_csv())  # ID,W_NAME,UNIT_ID,QUANTITY,PRICE,AMOUNT,BAR_CODE,A_ID,VAT_TYPE,STATUS
#
#     with open('stock.csv', newline='', encoding="UTF-8") as csvfile:
#
#         readerk = csv.reader(csvfile)
#
#         for row in readerk:
#             flag = False
#             good_id = row[0]
#             for k, v in global_stock.items():
#                 obj1 = StockItem(*row)
#                 if obj1 == (global_stock[k]):
#                     flag = True
#             if not flag:
#                 global_stock[good_id] = StockItem(*row)
#             else:
#                 temp = global_stock[good_id]
#                 # good_quantity
#                 row[3] = str(int(row[3]) + temp.QUANTITY)
#                 global_stock[good_id] = StockItem(*row)
#
#     with open('stock.csv', 'w', newline='', encoding="UTF-8") as csvfile:
#
#         writer = csv.writer(csvfile)
#
#         for k, item in global_stock.items():
#             writer.writerow(
#                 [item.ID, item.W_NAME, item.UNIT_ID, item.QUANTITY, item.PRICE, item.AMOUNT, item.BAR_CODE, item.A_ID,
#                  item.VAT_TYPE, item.STATUS])
#
#
# # Initialize a Label to display the User Input
# label = Label(win, text="", font="Courier 22 bold")
# label.grid(column=1)
#
# # Create an Entry widget to accept User Input
#
#
# entry = Entry(win, width=40)
# entry.focus_set()
# entry.grid(column=1)
#
# # Create a Button to validate Entry Widget
#
#
# ttk.Button(win, text="Okay", width=20, command=do).grid(column=1)
#
#
#
#
# scroll_bar = ttk.Scrollbar(win, orient="vertical")
#
# toggle_button = ttk.Button(win, text="Toggle Scrollbar", command=toggle_list_visibility)
# toggle_button.grid(row=0)
# # Create a listbox
# mylist = tk.Listbox(win, yscrollcommand=scroll_bar.set, width=40)
# mylist.grid(row=1)
# def open_sell_window():
#     sell_window = Tk()
#     sell_window.geometry("400x400")
#     sell_window.title("გაყიდე ბოზო")
#     win.configure(background="#A6F5C5")
#     sell_button1 = ttk.Button(sell_window,text="დამატება")
#     sell_button1.grid(row=0)
#
# sell_button = ttk.Button(win, text="sell",command=open_sell_window).grid(column=2)
#
#
#
# # Read data from 'stock.csv' and insert into the listbox
# update_stock_list()
#
#
#
# scroll_bar.config(command=mylist.yview)
#
#
#
#
#
# win.mainloop()
#
#

from app import App
from builders import *

if __name__ == "__main__":
    app = App("Vector", 600, 600)

    mainframe = FrameBuilder(app.get_root()).build().set_bg("orange").set_scale("news").place_element().set_geometry(
        (2, 2)).set_scaling_uniform(1)

    frame_top = FrameBuilder(mainframe.get_element()).build().set_bg("gray").set_scale("news").set_span(
        (1, 2)).place_element()
    frame_bottom_left = FrameBuilder(mainframe.get_element()).build().set_bg("white").set_position((1, 0)).set_scale(
        "news").place_element().set_geometry((2, 2)).set_scaling_uniform(1)
    frame_calculator = FrameBuilder(frame_bottom_left.get_element()).build().set_bg("blue").set_position(
        (1, 1)).set_scale(
        "news").place_element().set_geometry((4, 3)).set_scaling_uniform(1)
    frame_bottom_right = FrameBuilder(mainframe.get_element()).build().set_bg("white").set_position((1, 1)).set_scale(
        "news").place_element()
    frame_bottom_left.get_element().grid_propagate(False)
    frame_calculator_buttons = FrameBuilder(frame_bottom_left.get_element()).build().set_bg("green").set_scale(
        "news").set_position((1, 0)).place_element().set_geometry((3, 1)).set_scaling_uniform(1)

    calculator_value = StringVar()

    calculator_entry = EntryBuilder(frame_bottom_left.get_element()).build().set_scale("ews").set_span(
        (1, 2)).set_position(
        (0, 0)).place_element().set_font("Calibri 24").set_state("disabled").get_element().configure(
        textvariable=calculator_value, justify="right")

    for button_num in range(0, 3):
        extra_button = ButtonBuilder(frame_calculator_buttons.get_element()).build().set_position(
            (button_num, 0)).set_scale("news").place_element().set_text(f"Button {button_num}")

    buttons = []

    for num in range(9, 0, -1):
        row = 3 - round((num + 1) / 3)
        col = 2 if num % 3 == 0 else num % 3 - 1
        calculator_button = ButtonBuilder(frame_calculator.get_element()).build().set_text(num).set_position(
            (row, col)).set_scale("news").place_element()
        buttons.append(calculator_button)

    buttons[0].set_command(lambda: calculator_value.set(calculator_value.get() + "9"))
    app.get_root().bind("9", lambda e: buttons[0].get_element().invoke())
    buttons[1].set_command(lambda: calculator_value.set(calculator_value.get() + "8"))
    app.get_root().bind("8", lambda e: buttons[1].get_element().invoke())
    buttons[2].set_command(lambda: calculator_value.set(calculator_value.get() + "7"))
    app.get_root().bind("7", lambda e: buttons[2].get_element().invoke())
    buttons[3].set_command(lambda: calculator_value.set(calculator_value.get() + "6"))
    app.get_root().bind("6", lambda e: buttons[3].get_element().invoke())
    buttons[4].set_command(lambda: calculator_value.set(calculator_value.get() + "5"))
    app.get_root().bind("5", lambda e: buttons[4].get_element().invoke())
    buttons[5].set_command(lambda: calculator_value.set(calculator_value.get() + "4"))
    app.get_root().bind("4", lambda e: buttons[5].get_element().invoke())
    buttons[6].set_command(lambda: calculator_value.set(calculator_value.get() + "3"))
    app.get_root().bind("3", lambda e: buttons[6].get_element().invoke())
    buttons[7].set_command(lambda: calculator_value.set(calculator_value.get() + "2"))
    app.get_root().bind("2", lambda e: buttons[7].get_element().invoke())
    buttons[8].set_command(lambda: calculator_value.set(calculator_value.get() + "1"))
    app.get_root().bind("1", lambda e: buttons[8].get_element().invoke())

    button_backspace = ButtonBuilder(frame_calculator.get_element()).build().set_text("<-").set_position(
        (3, 0)).set_scale("news").place_element().set_command(lambda: calculator_value.set(calculator_value.get()[:-1]))
    app.get_root().bind("<BackSpace>", lambda e: button_backspace.get_element().invoke())
    button_zero = ButtonBuilder(frame_calculator.get_element()).build().set_text("0").set_position((3, 1)).set_scale(
        "news").place_element().set_command(lambda: calculator_value.set(calculator_value.get() + "0"))
    app.get_root().bind("0", lambda e: button_zero.get_element().invoke())
    button_clear = ButtonBuilder(frame_calculator.get_element()).build().set_text("C").set_position((3, 2)).set_scale(
        "news").place_element().set_command(lambda: calculator_value.set(""))
    app.run()

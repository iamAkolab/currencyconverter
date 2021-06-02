from tkinter import *

class CurrencyConvereter:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg = "dark grey")
        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Amount to convert"),grid(row=1, column = 1, sticky = W)

converter = CurrencyConvereter()

converter.resizable(width = False, height = False)
converter.mainloop()
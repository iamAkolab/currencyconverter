from tkinter import * 

class CurrencyConvereter: 
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        window.geometry("450x350")
        window.configure(bg = "dark grey")

        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Amount to convert").grid(row=1, column = 1, sticky = W)

        "Variable to be Convert with Entry Function"
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable = self.amounttoConvertVar, justify = RIGHT).grid(row = 1, column = 2)

        "Conversion Rate with Entry Function"
        self.convertionRate = StringVar()
        Entry(window, textvariable = self.convertionRate, justify = RIGHT).grid(row = 2, column = 2)

        "Converted Amount"
        self.convertedAmountVar = StringVar()
        lblConveretedAmount = Label(window, font = "Helvetica 12 bold", bg = "yellow", textvariable = self.convertedAmountVar).grid(row=3, column = 2, sticky = W)

converter = tk.CurrencyConvereter()
converter.mainloop()
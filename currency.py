from tkinter import * #Import whole module

class CurrencyConvereter(): 
    def __init__(self):
        window = Tk()                       # create application window
        window.title("Currency Converter")  # add title to application window
        window.geometry("450x350")          # specify size of the window
        window.configure(bg = "dark grey")  # Add background color

        # declaring our variables
        dropdownVar = StringVar()


        # Add a grid
        dropframe = Frame(window)
        dropframe.grid( column = 0, row = 0, sticky = (N,W,E,S) )
        dropframe.columnconfigure(0, weight = 1)
        dropframe.rowconfigure(0, weight = 1)
        dropframe.pack(pady = 100, padx = 100)

        # Dictionary with options
        choices = { 'Naira','Dollar','Pounds','Yen','Cedis'}
        dropdownVar.set('Naira')                 # set the default option
        
        popupMenu = OptionMenu(dropframe, dropdownVar, *choices)
        Label(dropframe, text="Amount to convert").grid(row = 1, column = 1)
        popupMenu.grid(row = 2, column =1)

        # on change dropdown value
        def change_dropdown(*args):
            print( dropdownVar.get() )

        # link function to change dropdown
        dropdownVar.trace('w', change_dropdown)

        # Adding Labels widgets to the application windows
        #slflabl = Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Amount to convert").grid(row=1, column = 1, sticky = W)

        # Variable to be Convert with Entry Function
        self.amounttoConvertVar = StringVar()
        #amounttoConvertVar = Entry(window, textvariable = self.amounttoConvertVar, justify = RIGHT).grid(row = 1, column = 2)

        # Conversion Rate with Entry Function
        self.conversionRate = StringVar()
        #Entry(window, textvariable = self.conversionRate, justify = RIGHT).grid(row = 2, column = 2)

        # Converted Amount
        self.convertedAmountVar = StringVar()
        # = Label(window, font = "Helvetica 12 bold", bg = "yellow", textvariable = self.convertedAmountVar).grid(row=3, column = 2, sticky = E)

        #create convert and clear buttons
        btbConvertedAmount = Button(window, text = "Convert", font = "Helvetica 12 bold", bg = "blue", fg = "white", command = self.ConvertedAmount).grid(row = 4, column = 2, sticky = E)
        #btbdelete_all = Button(window, text = "Clear", font = "Helvetica 12 bold", bg = "red", fg = "white", command = self.delete_all).grid(row = 4, column = 6, padx = 25, pady = 25, sticky = E)

        window.mainloop() # run the application

    #Function to do the conversion. stores inputs and performs computation
    def ConvertedAmount(self):
        amt = float(self.conversionRate.get())
        convertedAmountVar = float( self.amounttoConvertVar.get() )* amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))
        
    # Function to clear inputs
    def delete_all(self):
        self.amounttoConvertVar.set("")
        self.conversionRate.set("")
        self.convertedAmountVar.set("")

CurrencyConvereter()
from tkinter import * #Import whole module

class CurrencyConvereter(): 
    def __init__(self):
        window = Tk()                       # create application window
        window.title("Currency Converter")  # add title to application window
        window.geometry("400x300")          # specify size of the window
        window.configure(bg = "dark grey")  # Add background

        # Dictionary with options
        choices = { 'Naira','Dollar','Pounds','Yen','Cedis'} 
        
        # declaring our variables
        currencyVariable = StringVar()   # Variable for the first dropdown
        currencyVariable.set("Naira")    # set the default option

        convertedVariable = StringVar()  # Variable for the first dropdowm
        convertedVariable.set('Dollar')  # set the default option

        self.amountToConvert = StringVar()
        self.convertedAmount = StringVar()
        
        #From and to label
        fromLabel = Label(window, text = "From", fg = "black")
        fromLabel.grid(row = 0 , column = 0, padx = 30, pady = 30)
        
        toLabel = Label(window, text = "To", fg = "black")
        toLabel.grid(row = 1 , column = 0,padx = 30, pady = 30)

        #menus
        popupMenu1 = OptionMenu(window, currencyVariable, *choices)
        popupMenu1.grid(row = 0 , column = 1,pady = 15, padx = 15)

        popupMenu2 = OptionMenu(window, convertedVariable, *choices)
        popupMenu2.grid(row = 1 , column = 1,pady = 15, padx = 15)
       
        # entries
        fromEntry = Entry(window, textvariable = self.amountToConvert, width = 14)
        fromEntry.grid(column = 2, row = 0)     

        toEntry = Label(window, textvariable = self.convertedAmount, width = 14)
        toEntry.grid(column = 2, row = 1)     
        
        # on change dropdown value
        def change_dropdown1(*args):
            print( currencyVariable.get() )
        
        def change_dropdown2(*args):
            print( convertedVariable.get() )

        # link function to change dropdown
        currencyVariable.trace('w', change_dropdown1)
        convertedVariable.trace('w', change_dropdown2)

        # the variables
        self.popmenu_out1 = currencyVariable
        self.popmenu_out2 = convertedVariable

        # create calculate button
        calculate_btn = Button(window, text = "Calculate", bg = "green", fg = "white", command = self.calculate)
        calculate_btn.grid(column = 1, row = 3, padx = 50, pady = 50)

        # create the clear buttin
        clear_btn = Button(window, text = "Clear", bg = "red", fg = "black", command = self.clear)
        clear_btn.grid(column = 2, row = 3, padx = 50, pady = 50)

        window.mainloop()

    def calculate(self):
        convertedCurr = IntVar()
        curr_amount = float(self.amountToConvert.get())
        from_currency = self.popmenu_out1.get()
        to_currency = self.popmenu_out2.get()

        if from_currency == to_currency:
            self.convertedAmount.set(curr_amount)

        elif from_currency == "Naira": #Naira selected first
            if to_currency == "Dollar":
                self.convertedAmount.set(round(curr_amount / 500,2) )
            elif to_currency == "Pounds":
                self.convertedAmount.set(round(curr_amount / 720, 2) )
            elif to_currency == "Yen":
                self.convertedAmount.set(round(curr_amount / 64, 2) )
            elif to_currency == "Cedis":
                self.convertedAmount.set(round(curr_amount / 70,2) )

        elif from_currency == "Dollar": # Dollar selected first
            if to_currency == "Naira":
                self.convertedAmount.set(round(curr_amount * 500, 2) )
            elif to_currency == "Pounds":
                self.convertedAmount.set(round(curr_amount * 0.71, 2) )
            elif to_currency == "Yen":
                self.convertedAmount.set(round(curr_amount * 6.40, 2) )
            elif to_currency == "Cedis":
                self.convertedAmount.set(round(curr_amount * 5.78, 2) )

        elif from_currency == "Pounds":  #Pounds selected first
            if to_currency == "Dollar":
                self.convertedAmount.set(round(curr_amount / 0.71, 2) )
            elif to_currency == "Naira":
                self.convertedAmount.set(round(curr_amount * 720, 2) )
            elif to_currency == "Yen":
                self.convertedAmount.set(round(curr_amount * 9.03, 2) )
            elif to_currency == "Cedis":
                self.convertedAmount.set(round(curr_amount * 8.16, 2) )

        elif from_currency == "Yen":  #Yen selected first
            if to_currency == "Dollar":
                self.convertedAmount.set(round(curr_amount / 6.40, 2) )
            elif to_currency == "Pounds":
                self.convertedAmount.set(round(curr_amount / 9.03, 2) )
            elif to_currency == "Naira":
                self.convertedAmount.set(round(curr_amount * 70, 2) )
            elif to_currency == "Cedis":
                self.convertedAmount.set(round(curr_amount / 0.90) )

        elif from_currency == "Cedis":    #Cedis selected first
            if to_currency == "Dollar":
                self.convertedAmount.set(round(curr_amount / 5.78, 2) )
            elif to_currency == "Pounds":
                self.convertedAmount.set(round(curr_amount / 8.16, 2) )
            elif to_currency == "Yen":
                self.convertedAmount.set(round(curr_amount * 0.90, 2) )
            elif to_currency == "Naira":
                self.convertedAmount.set(round(curr_amount * 70, 2) )

    def clear(self):
        self.amountToConvert.set("")
        self.convertedAmount.set("")
        self.currencyVariable.set('Naira')
        self.convertedVariable.set('Dollar')
        

CurrencyConvereter()
#'Dollar','Pounds','Yen','Cedis'
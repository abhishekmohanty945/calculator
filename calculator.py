from tkinter import *

def buttonclick(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)

def clearall():
    global operator
    operator = ""
    text_input.set("")

def equals():
    global operator
    ans = str(eval(operator))
    text_input.set(ans)
    operator = ""

calculator = Tk()

calculator.title("Calculator")

operator = " "

text_input = StringVar()

textDisplay = Entry(calculator, font = ("ariel", 20, "bold"),             
                    textvariable = text_input, bd = 30, insertwidth = 4, bg = "#EEEEEE",
                    justify = "right").grid(columnspan = 5)

######################################################################################################################

button7 = Button(calculator, padx = 16, pady = 16, bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "7", bg = "light grey", command = lambda: buttonclick(7)).grid(row = 1, column = 1)

button8 = Button(calculator, padx = 16, pady = 16, bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "8", bg = "light grey", command = lambda: buttonclick(8)).grid(row = 1, column = 2)

button9 = Button(calculator, padx = 16, pady = 16, bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "9", bg = "light grey", command = lambda: buttonclick(9)).grid(row = 1, column = 3)

multiplication = Button(calculator, padx = 16, pady = 16, bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "*", bg = "light grey", command = lambda: buttonclick("*")).grid(row = 1, column = 4)

######################################################################################################################

button4 = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "4", bg = "light grey", command = lambda: buttonclick(4)).grid(row = 2, column = 1)

button5 = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "5", bg = "light grey", command = lambda: buttonclick(5)).grid(row = 2, column = 2)

button6 = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "6", bg = "light grey", command = lambda: buttonclick(6)).grid(row = 2, column = 3)

division = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "/", bg = "light grey", command = lambda: buttonclick("/")).grid(row = 2, column = 4)

######################################################################################################################

button1 = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "1", bg = "light grey", command = lambda: buttonclick(1)).grid(row = 3, column = 1)

button2 = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "2", bg = "light grey", command = lambda: buttonclick(2)).grid(row = 3, column = 2)

button3 = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "3", bg = "light grey", command = lambda: buttonclick(3)).grid(row = 3, column = 3)

addition = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "+", bg = "light grey", command = lambda: buttonclick("+")).grid(row = 3, column = 4)

######################################################################################################################

clear = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "C", bg = "light grey", command = lambda: clearall()).grid(row = 4, column = 1)

button0 = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "0", bg = "light grey", command = lambda: buttonclick(0)).grid(row = 4, column = 2)

equals = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "=", bg = "light grey", command = equals).grid(row = 4, column = 3)

substraction = Button(calculator, padx = 16, pady = 16,bd = 10, fg = "black", font = ("arial", 20, "bold"),
                 text = "-", bg = "light grey", command = lambda: buttonclick("-")).grid(row = 4, column = 4)

######################################################################################################################

calculator.mainloop()

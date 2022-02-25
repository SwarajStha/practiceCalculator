from tkinter import *
import math
import tkinter.font as tkFont

root = Tk()
root.title("Calculator")
root.iconbitmap('c:/Users\swara\Documents\Program Code\Python\Calculator.ico')

fontSize = tkFont.Font(size=25)
fontSizeWords1 = tkFont.Font(size=10)
fontSizeSymbols = tkFont.Font(size=10)

entered = Entry(root, width =40, borderwidth= 3)
entered.grid(row=0, column=0, columnspan=3, padx=18, pady=30)

def button_pressed(number):
    current = entered.get()
    entered.delete(0, END)
    entered.insert(0, str(current) + str(number))

def button_clear():
    entered.delete(0, END)

def button_add():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()
    
    global f_num 
    global math1
    math1 = "addition"
    f_num = float(first_number)
    entered.delete(0,END)

def button_subtract():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    math1 = "subtraction"
    f_num = float(first_number)
    entered.delete(0,END)

def button_multiply():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    math1 = "multiplication"
    f_num = float(first_number)
    entered.delete(0,END)

def button_divide():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    math1 = "division"
    f_num = float(first_number)
    entered.delete(0,END)

def button_exponent():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    math1 = "exponent"
    f_num = float(first_number)
    entered.delete(0,END)
    return

def button_radian():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    math1 = "radian"
    f_num = float(first_number)
    entered.delete(0,END)
    return   

def button_root():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    f_num = float(math.sqrt(first_number))
    math1 = "root"
    entered.delete(0,END)
    return

def button_factorial():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    f_num = math.factorial(float(first_number))
    math1 = "factorial"
    entered.delete(0,END)
    return
    
def button_sin():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    rad = math.radians(float(first_number))
    f_num = math.sin(float(rad))
    math1 = "sin"
    entered.delete(0,END)
    return

def button_cos():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    rad = math.radians(float(first_number))
    f_num = math.cos(float(rad))
    math1 = "cos"
    entered.delete(0,END)
    return

def button_tan():
    if  entered.get() == "π":
        first_number = math.pi
    else:
        first_number = entered.get()

    global f_num 
    global math1
    rad = math.radians(float(first_number))
    #if rad == 0.5235987755982988:
       # f_num = 0
    #else:
    f_num = math.tan(float(rad))
    math1 = "tan"
    entered.delete(0,END)
    return

def button_equal():
    if  entered.get() == "π":
        second_number = math.pi
    else:
        second_number = entered.get()

    entered.delete(0, END)

    if math1 == "addition":
        entered.insert(0, float(f_num + float(second_number)))
    elif math1 == "subtraction":
        entered.insert(0, float(f_num - float(second_number)))
    elif math1 == "multiplication":
        entered.insert(0, float(f_num * float(second_number)))
    elif math1 == "division":
        entered.insert(0, float(f_num/float(second_number)))
    elif math1 == "exponent":
        entered.insert(0, float(f_num**float(second_number)))
    elif math1 == "radian":
        entered.insert(0, float(math.radians(f_num)))
    elif math1 == "root":
        entered.insert(0, f_num)
    elif math1 == "factorial":
        entered.insert(0, f_num)
    elif math1 == "sin":
        entered.insert(0, f_num)
    elif math1 == "cos":
        entered.insert(0, f_num)
    elif math1 == "tan":
        entered.insert(0, f_num)


#Define buttons

Button_1 = Button(root, text="1", padx=25, command= lambda: button_pressed(1), bg="#ffffff")
Button_1['font']= fontSize
Button_2 = Button(root, text="2", padx=25, command= lambda: button_pressed(2), bg="#ffffff")
Button_2['font']= fontSize
Button_3 = Button(root, text="3", padx=25, command= lambda: button_pressed(3),bg="#ffffff")
Button_3['font']= fontSize
Button_4 = Button(root, text="4", padx=25, command= lambda: button_pressed(4),bg="#ffffff")
Button_4['font']= fontSize
Button_5 = Button(root, text="5", padx=25, command= lambda: button_pressed(5),bg="#ffffff")
Button_5['font']= fontSize
Button_6 = Button(root, text="6", padx=25, command= lambda: button_pressed(6),bg="#ffffff")
Button_6['font']= fontSize
Button_7 = Button(root, text="7", padx=25, command= lambda: button_pressed(7),bg="#ffffff")
Button_7['font']= fontSize
Button_8 = Button(root, text="8", padx=25, command= lambda: button_pressed(8),bg="#ffffff")
Button_8['font']= fontSize
Button_9 = Button(root, text="9", padx=25, command= lambda: button_pressed(9),bg="#ffffff")
Button_9['font']= fontSize
Button_0 = Button(root, text="0", padx=25, pady=1, command= lambda: button_pressed(0),bg="#ffffff")
Button_0['font']= fontSize

Button_Decimal = Button(root, text=" .", padx=40, pady=22, command= lambda: button_pressed("."))
Button_Root = Button(root, text="√ ", padx=35, pady=20, command= button_root, bg="#d7d3d3")
Button_Root['font'] = tkFont.Font(size=11)
Button_Pi = Button(root, text="π", padx=38, pady=19, command= lambda: button_pressed("π"), bg="#d7d3d3")
Button_Pi['font'] = fontSizeSymbols
Button_Factorial = Button(root, text="n!", padx=35, pady=18, command= button_factorial, bg="#d7d3d3")
Button_Factorial['font'] = tkFont.Font(size=11)
Button_Radian = Button(root, text=" rad ", padx=29, pady=19, command= button_radian, bg="#d7d3d3")
Button_Radian['font'] = fontSizeWords1
Button_Exponent = Button(root, text="xʸ", padx=40, pady=14, command= button_exponent, bg="#d7d3d3")
Button_Exponent['font'] = tkFont.Font(size=11)

Button_Clear = Button(root, text="CLR", padx=30, pady=30, command= button_clear)
Button_Clear['font']= tkFont.Font(size = 11)

Button_Add = Button(root, text="+", padx=39, pady=14, command= button_add)
Button_Add['font'] = tkFont.Font(size=14)
Button_Subtract = Button(root, text=" - ", padx=35, pady=14, command= button_subtract)
Button_Subtract['font'] = tkFont.Font(size=15)
Button_Multiply = Button(root, text="×", padx=40, pady=18, command= button_multiply)
Button_Multiply['font'] = tkFont.Font(size=13)
Button_Divide = Button(root, text="÷", padx=39, pady=15, command= button_divide)
Button_Divide['font'] = tkFont.Font(size=15)
Button_Sin = Button(root, text="sin", padx=34, pady=15, command= button_sin, bg="#c1bbba")
Button_Sin['font'] = fontSizeWords1
Button_Cos = Button(root, text="cos", padx=32, pady=15, command= button_cos,bg="#c1bbba")
Button_Cos['font'] = fontSizeWords1
Button_Tan = Button(root, text="tan", padx=33, pady=15, command= button_tan,bg="#c1bbba")
Button_Tan['font'] = fontSizeWords1

Button_Equal = Button(root, text="=", padx=36, pady=12, command= button_equal, bg="#bbbec1")
Button_Equal['font'] = tkFont.Font(size=17)

#Put buttons on the screen

Button_1.grid(row=5, column=0)
Button_2.grid(row=5, column=1)
Button_3.grid(row=5, column=2)

Button_4.grid(row=4, column=0)
Button_5.grid(row=4, column=1)
Button_6.grid(row=4, column=2)

Button_7.grid(row=3, column=0)
Button_8.grid(row=3, column=1)
Button_9.grid(row=3, column=2)

Button_0.grid(row=6, column=1)

Button_Decimal.grid(row=6, column=0)
Button_Root.grid(row=6, column=2)
Button_Pi.grid(row=2,column=0)
Button_Factorial.grid(row=2,column=1)
Button_Radian.grid(row=2,column=2)
Button_Exponent.grid(row=1,column=3)

Button_Clear.grid(row=0, column=3)

Button_Add.grid(row=2, column=3)
Button_Subtract.grid(row=3, column=3)
Button_Multiply.grid(row=4, column=3)
Button_Divide.grid(row=5, column=3)

Button_Sin.grid(row=1,column=0)
Button_Cos.grid(row=1,column=1)
Button_Tan.grid(row=1,column=2)

Button_Equal.grid(row=6, column=3)

root.mainloop()
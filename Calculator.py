




from tkinter import *

def click_button(number):
    global enter_keyword
    enter_keyword += str(number)
    text.set(enter_keyword)

def calculate_result():
    global enter_keyword
    try:
        result = str(eval(enter_keyword))
        text.set(result)
        enter_keyword = ''
    except SyntaxError or ZeroDivisionError:
        text.set("Error")
        enter_keyword = ''

def clear_button():
    text.set('')
    global enter_keyword
    enter_keyword = ''

window = Tk()
window.geometry("350x450")
window.title("Calculator ")
label = Label(window, text="CALCULATOR", bg='grey', font=("Times", 30, 'bold'))
label.pack(side=TOP)
window.config(background='dark grey')
window.resizable(0,0)

text = StringVar()
enter_keyword = ""

text_enter = Entry(window, font=("Serif", 15, 'bold'), textvar=text, width=35, bd=14, bg='grey')
text_enter.pack()




button_7 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(7), text="7", font=("serif", 16, 'bold'))
button_7.place(x=12, y=100)

button_8 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(8), text="8", font=("serif", 16, 'bold'))
button_8.place(x=80, y=100)

button_9 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(9), text="9", font=("serif", 16, 'bold'))
button_9.place(x=150, y=100)



button_6 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(6), text="6", font=("serif", 16, 'bold'))
button_6.place(x=10, y=170)

button_5 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(5), text="5", font=("serif", 16, 'bold'))
button_5.place(x=75, y=170)

button_4 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(4), text="4", font=("serif", 16, 'bold'))
button_4.place(x=140, y=170)


button_3 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(3), text="3", font=("serif", 16, 'bold'))
button_3.place(x=10, y=240)

button_2 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(2), text="2", font=("serif", 16, 'bold'))
button_2.place(x=75, y=240)

button_1 = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button(1), text="1", font=("serif", 16, 'bold'))
button_1.place(x=140, y=240)

button_0 = Button(window, padx=80, pady=14, bd=4, bg='white', command=lambda: click_button(0), text="0", font=("serif", 16, 'bold'))
button_0.place(x=10, y=310)


button_add = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button("+"), text="+", font=("serif", 16, 'bold'))
button_add.place(x=205, y=100)

button_sub = Button(window, padx=14, pady=16, bd=4, bg='white', command=lambda: click_button("-"), text="-", font=("serif", 16, 'bold'))
button_sub.place(x=205, y=170)

button_mul = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button("*"), text="*", font=("serif", 16, 'bold'))
button_mul.place(x=205, y=240)

button_div = Button(window, padx=14, pady=14, bd=4, bg='white', command=lambda: click_button("/"), text="/", font=("serif", 16, 'bold'))
button_div.place(x=205, y=310)

button_clear = Button(window, padx=14, pady=119, bd=4, bg='white', text="CE", command=clear_button, font=("serif", 16, 'bold'))
button_clear.place(x=270, y=100)

button_equal = Button(window, padx=151, pady=14, bd=4, bg='white', command=calculate_result, text="=", font=("serif", 16, 'bold'))
button_equal.place(x=10, y=380)

window.mainloop()






from tkinter import *               # alles von tkinter importieren

root = Tk()
root.title("GUI Tutorial")
bg2 = Canvas(root, width=400, height= 400, background= "#66E5FF")
bg2.grid(row=0, column=0)

e = Entry(bg2, width=40, bg="#B2FFFF", fg="black" , borderwidth=1, highlightthickness=3)
e.config(highlightbackground = "#B2F0FF", highlightcolor= "white")
e.grid(row=0, column=0, columnspan=3, ipady=20) # padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(1, f_num + int(second_number))
    e.insert(0, "Ergebnis: ")

# Define Buttons

button_1 = Button(bg2, text="1", bg="#FF997F", fg="white", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(bg2, text="2", bg="#FF4C4C", fg="white", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(bg2, text="3", bg="#FF4C00", fg="white", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(bg2, text="4", bg="#CCFF00", fg="black", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(bg2, text="5", bg="#99FF00", fg="black", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(bg2, text="6", bg="#66E500", fg="black", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(bg2, text="7", bg="#99CCFF", fg="white", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(bg2, text="8", bg="#6699FF", fg="white", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(bg2, text="9", bg="#3399FF", fg="white", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(bg2, text="0", bg="#FF0066", fg="white", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(bg2, text="+", bg="#FF3366", fg="black", padx=39, pady=20, command=button_add)
button_equal = Button(bg2, text="=", bg="#B2FFFF", fg="black", padx=80, pady=20, command=button_equal)
button_clear = Button(bg2, text="C", bg="#FF6699", fg="black", padx=40, pady=20, command=button_clear)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_equal.grid(row=5, column=0, columnspan=3) #, padx=2, pady=10)

root.mainloop()
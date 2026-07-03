from tkinter import*

def button_press(num):
    pass

def equals():
    pass

def clear(num):
    pass

window = Tk()
window.title("Calculadora da Gabs")
window.geometry("500X500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas', 20))

label = Label(window, textvariable = equation_label)
window.mainloop()
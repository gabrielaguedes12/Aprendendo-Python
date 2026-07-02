#GUI - Graphical User Interface
#Function - é um pequeno segmento de código que pode ser executado
#Module- Uma coleção de funções que o usuario consegue chamar

from tkinter import * 
#1 passo: criar uma janela principal
root = Tk()

#2° passo: criar um elemento
word = Label(root, text="Hello World!")
word.pack()

#Pop up para manter a janela aberta
root.mainloop()

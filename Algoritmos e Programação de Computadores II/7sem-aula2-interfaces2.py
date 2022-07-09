#aceita entrada de valores
from tkinter import Tk, Button, Label, Entry
from tkinter.messagebox import showinfo
from time import strftime, strptime


def clicked():
    global entry            #importar o atibuto entry: texto digitado
    date = entry.get()      #data digitada
    weekday = strftime('%A', strptime(date, '%b %d, %Y'))   #dia da semana
    showinfo(message='{} was a {}'.format(date, weekday))   #exibe msg na tela


root = Tk()         #janela
label = Label(root, text='Digite uma data:')
label.grid(row=0, column=0)     #organiza os componentes na tela principal
entry = Entry(root)             #componente de inserção de texto
entry.grid(row=0, column=1)     # grid :adicionar como que vai aparecer na tela
button = Button(root, text='Clique', command=clicked)
button.grid(row=1, column=0, columnspan=2)
root.mainloop()

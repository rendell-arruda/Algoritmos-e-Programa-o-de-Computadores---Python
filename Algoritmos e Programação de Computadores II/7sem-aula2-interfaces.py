#programação orientada a ações
#clica no botão e mostra data e hora
from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo     # MANEIRA DE EXIBIR JANELA DE INFORMAÇÃO
from time import strftime, localtime        # classes para obter hora atual e formatação

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S%p\n', localtime()) #objeto time,localtime() retorna hora local
    showinfo(message=time) #mostrar na tela que contem as informações

root = Tk()     #cria a janela principal
button = Button(root, text='Clique', command=clicked) #cria o botão, e o command serve para monitorar o evento no caso clique
button.pack()               #empacota a janela com o botão
root.mainloop()             #mostra na tela o pacote


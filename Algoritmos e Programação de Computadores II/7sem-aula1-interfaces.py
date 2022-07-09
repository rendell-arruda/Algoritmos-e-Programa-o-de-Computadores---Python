'''
#inicio da aula
#para invocar a janela importaremos a classe tk do modulo tkinter

from tkinter import Tk, Label   # importando a biblioteca  tkinter e a classe Tk
root = Tk()                     # criaremos um objeto usando a classe Tk
root.mainloop()                 # para criar a janela invocaremos o metodo mainloop()

## a classe Label foi importada la em cima
# o widget Label é utilizado para exibir texto na janela
hello = Label(master=root, text='Hello World')  #Objeto da classe Label e seus parametros. o atributo
                                                # master indica qual a janela vai aparecer. o atributo text é o proprio texto
hello.pack()                        #metodo pack fornece as diretivas ao sistema empacotamento dos componentes na janela
root.mainloop()
##
'''
#programa para exibir foto e msg
from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()                                                 #objeto root da class tk
photo = PhotoImage(file='computer.gif').subsample(2)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text='Olá alunos da Univesp')
text.pack(side=BOTTOM)                                      # pack empacota o conteudo na janela e indica a sua posiçao
root.mainloop()


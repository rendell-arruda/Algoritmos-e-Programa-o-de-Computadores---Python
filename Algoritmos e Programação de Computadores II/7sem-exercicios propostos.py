##
#Problema Prático 9.1
#Escreva um programa peaceandlove.py que cria esta GUI:
from tkinter import Tk, Label, PhotoImage, BOTH, RIGHT, LEFT

raiz = Tk()

label1 = Label(raiz, text='Paz e amor', background='black', width=20, height=5, foreground='white', font=('Helvetica', 18,'italic'))
label1.pack(side=LEFT)

photo = PhotoImage(file='anarchy-peace-sign.gif')
label2 = Label(raiz, image=photo)
label2.pack(side=RIGHT, expand=True, fill=BOTH)
raiz.mainloop()
##
'''
#Problema Prático 9.2 - NAO SAIU

#Implemente a função cal() que aceita como entrada um ano e um mês (um número entre 1 e 12) e começa com uma GUI que
# mostra o calendário correspondente.
from calendar import monthrange
days = ['Seg','Ter','Qua', 'Qui', 'Sex', 'Sab', 'Dom']
for i in range(7):
    label = Label(raiz, text=days[i])
    label.grid(row=0, column=i)
weekday, numDays = monthrange(year, month)
week = 1
for i in range(1, numDays+1):
    label = Label(root, text=str(i))
    label.grid(row=week, column=weekday)

weekday += 1
if weekday > 6:
    week += 1
    weekday = 0
'''

##
#Problema Prático 9.3

#Implemente um aplicativo GUI que contenha dois botões rotulados “Hora local” e “Hora de Greenwich”.
# Quando o primeiro botão é pressionado, a Hora local deverá aparecer no shell. Quando o segundo botão é pressionado,
# a Hora de Greenwich deve ser exibida.
from tkinter import Tk, Button,RIGHT, LEFT
from time import strftime, localtime
def greenwich():
    'exibe informações de dia e hora de Greenwich'
    time = strftime('Dia: %d %b %Y\n Hora: %H:%M:%S %p \n', localtime())
    print('Hora local \n + time')

#Botão de hora local
button1 = Button(raiz, text='Hora local', command=local)
button1.pack(side=LEFT)

#Botão de hora de GreenWich
buttong = Button(root,text='Hora de Greenwich', command=greenwich)
buttong.pack(side=RIGHT)
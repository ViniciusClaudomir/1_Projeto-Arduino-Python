# -*- coding: UTF-8 -*-
# O script foi desenvolvido para ser
# usado inicialmente em smartphone,
# com resolução de 1080x1920, caso
# for usado em PC, será necessario alterar
# a resolução dos widgets : quit e but 1

import socket
from tkinter import *


def lig():
    imp()


def imp(var_1=None):
    try:
        s = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM)
        s.connect(("Seu ip aqui", 3333))#estabelece a conexão entre o celular e o pc
        status()#retorna para o Entry, se a conexão foi realizada com sucesso
        str_recv = s.recv(1024)
        print(str(str_recv))
        var_2 = str(v.get())
        str_send = var_2
        s.send(bytes(str_send, "utf-8"))#envia o comando para o computador
        str_recv = s.recv(1024)
        print(str(str_recv))
        s.close
    except:
        ent1 = Entry(ard)
        ent1.insert("0", "Servidor desligado")
        ent1.grid(row=1, column=3)
        ent1["fg"] = "White"
        ent1["bg"] = "red"


ard = Tk()#tela tkinter
v = IntVar()# variavel dos radiobuttons


def status():
    b = str(v.get())
    ent1 = Entry(ard)
    ent1.insert("0", "Online")
    ent1.grid(row=1, column=3)
    ent1["fg"] = "green"


ent = Entry(ard)
ent.insert("0", "Offline")
ent.grid(row=1, column=3)
ent["fg"] = "red"
##############################Aqui é a entrada de dados, cada botão, do tipo radio button, recebe um value, equivalente a sua função no arduino
#"grid" orientação do widget, em relação a linha e coluna.
bot1 = Radiobutton(text="azul", width=15, height=2, variable=v, value=1)#led
bot1.grid(row=1, column=1)
bot1["bg"] = "blue"

bot2 = Radiobutton(text="vermelho", width=15, height=2, variable=v, value=2)#led
bot2.grid(row=2, column=1)
bot2["bg"] = "red"

cort = Radiobutton(text="cortina", width=15, height=2, variable=v, value=9)#relé
cort.grid(row=3, column=1)

but = Button(ard, text="Enviar", width=10, command=imp)#chama a função imp, responsavel por enviar os comandos

but.place(x=435, y=800)#resolução, caso use em pc, altere, ou coloque em grid

but1 = Button(ard, text="conect_server", width=10, height=1, command=lig)#testa a conexão com o servidor
but1.grid(row=2, column=3)

pl = Label(ard, text="Pressione connect_server\n para verificar a conexão", height=2)
pl.grid(row=3, column=3)
pl["bg"] = "black"
pl["fg"] = "red"

quit = Button(text="Sair", width=10, command=ard.destroy)
quit.place(x=435, y=1200)#resolução, caso use em pc, altere, ou coloque em grid
ard.title("arduino")
ard["bg"] = "green"
ard.geometry("1070x1910")#resolução do dispostivo

ard.mainloop()# responsavel por criar a tela

import serial
import time
try:
   con = serial.Serial('com3', 9600)#sera inserido a porta onde o arduino estar conectado.
   con.write(b'9')#para manter o relé desligado, declarei ele logo no inicio do programa
except:
    print("Por favor,verifique se o arduino foi conectado corretamente!!!")
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('Seu ip aqui', 3333))#aqui será informado o IP para realizar a conexão entre o PC e o SMARTPHONE
s.listen(5)#limite de usuarios
flag = 0
master = True
def cor():# mandar os comandos para o arduino, com base  no valor enviado pelo smartphone
    if str_recv == b'2':
        print("test @")
        con.write(b'0')#0 apaga
        time.sleep(1)
        con.write(b'2')#2 acende
    if str_recv == b'1':
        con.write(b'3')#3 apaga
        time.sleep(1)
        con.write(b'1')#1 acende
    if str_recv == b'9':# é a condição do relé, ela não possui um "apaga", pois no sketch do arduino
        #ela é configura para apagar depois de um delay de 600, tempo que foi o suficiente para o teste da cortina
        con.write(b'9')
while master:
    connect, addr = s.accept()
    var_0 = "conectado"
    print("                   ")
    str_return = var_0
    connect.sendto(bytes(str_return, 'utf-8'), addr)
    str_recv, temp = connect.recvfrom(1024)
    print(str_recv)
    cor()
    b = str_recv
    con.write(b)
    str_return =  str(str_recv)
    connect.sendto(bytes(str_return, 'utf-8'), addr)
    connect.close()

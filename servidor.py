# coding: utf-8 
 
import socket, threading

def conecta( cliente ): 
    while True: 
        try:
            mensagem = cliente.recv(2048)
            print (mensagem.decode())
        except:
            break 
 
#Listen. (porta que vai ficar escutando) 
listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
listen.bind( ('localhost', 8088) ) 
listen.listen( 0 ) 
print('SERVIDOR LIGADO') 
 

# Estabelecendo conexão com o cliente . 
while True: 
    cliente, endereco = listen.accept() 
    thread = threading.Thread( target = conecta, args = [cliente] ).start()
            

# coding: utf-8 
import socket, threading             
  
def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

    try:
        cliente.connect(('localhost', 8088))
    except:
        return

    usr = input('Usuário: ')

    thread = threading.Thread(target=msg, args=[cliente, usr]).start()


def msg(client, usr):
    while True:
        try:
            mensagem = input("digite uma mensagem:")
            client.sendall(f'{usr}---> {mensagem}'.encode())
        except:
            return

main()
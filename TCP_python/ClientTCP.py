import socket #importa modulo socket
import threading
import sys

TCP_IP = '192.168.15.10' # endereço IP do servidor 
TCP_PORTA = 41903      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024

MENSAGEM  = input("Digite sua mensagem para o servidor: ")

# Criação de socket TCP do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conecta ao servidor em IP e porta especifica 
cliente.connect((TCP_IP, TCP_PORTA))

# envia mensagem para servidor 
cliente.send(MENSAGEM.encode('UTF-8'))

class myThread (threading.Thread):
   def __init__(self, threadID, cliente):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.cliente = cliente
   def run(self):
      print ("Starting Thread" + str(self.threadID))
      chat(self.threadID, self.cliente)
      print ("Exiting Thread" + str(self.threadID))

def chat(threadID, cliente):
    quit = ("QUIT").encode('UTF-8')
    if (threadID == 1):
        print ("#########################\nChat\n#########################")
        while 1:
            #dados retirados da mensagem recebida
            data, addr = cliente.recvfrom(1024)
            print ("Mensagem do servidor:", data)
            if data == quit:
                cliente.send(("Chat encerrado pelo servidor!").encode('UTF-8'))
                cliente.close()
                print("Chat encerrado pelo servidor")
                break
    else:
        while 1:
            mensagem = input()
            if mensagem != "QUIT":
                cliente.send(mensagem.encode('UTF-8'))
            else:
                cliente.send(("Chat encerrado pelo cliente!").encode('UTF-8'))
                cliente.close()
                print("Chat encerrado pelo cliente!")

thread1 = myThread(1, cliente)
thread2 = myThread(2, cliente)
thread1.daemon = True
thread2.daemon = True

thread2.start()
thread1.start()

while 1:
    if not(thread1.is_alive()) or not(thread2.is_alive()):
        sys.exit()
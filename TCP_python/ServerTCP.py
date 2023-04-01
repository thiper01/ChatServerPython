import socket #importa modulo socket
import threading

TCP_IP = '192.168.15.10' # endereço IP do servidor 
TCP_PORTA = 41903       # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024     # definição do tamanho do buffer
 
class myThread (threading.Thread):
   def __init__(self, threadID, conn):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.conn = conn
   def run(self):
      print ("Starting Thread" + str(self.threadID))
      chat(self.threadID, self.conn)
      print ("Exiting Thread" + str(self.threadID))

def chat(threadID, conn):
    if (threadID == 1):
        print ("#########################\nChat\n#########################")
        while 1:
            #dados retidados da mensagem recebida
            data = conn.recv(TAMANHO_BUFFER)
            if data: 
                if data == (("Chat encerrado pelo servidor!").encode('UTF-8')):
                    break
                print ("Mensagem do cliente:", data)
                if data == ("Chat encerrado pelo cliente!").encode('UTF-8'):
                    break
    else:
        while 1:
            mensagem = input()
            conn.send(mensagem.encode('UTF-8'))
            if mensagem == "QUIT":
                print("Chat encerrado pelo servidor!")
                break
        


# Criação de socket TCP
# SOCK_STREAM, indica que será TCP.
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP e porta que o servidor deve aguardar a conexão
servidor.bind((TCP_IP, TCP_PORTA))

#Define o limite de conexões. 
servidor.listen(10)

while 1:
    print("Servidor dispoivel na porta 41903 e escutando.....") 
    # Aceita conexão 
    conn, addr = servidor.accept()
    print ('Endereço conectado:', addr)



    # Create new threads
    thread1 = myThread(1, conn)
    thread2 = myThread(2, conn)

    thread1.start()
    thread2.start()

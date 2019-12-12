import socket
from threading import Thread
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client.connect(('0.0.0.0', 8085))
#msg="I am Here"
#b = bytes(msg, 'utf-8')
#client.send(b)
#from_server = client.recv(4096)

#print(from_server)

def sent_Message(TEXT):
    b=bytes(TEXT,'utf-8')
    client.send(b)

def recv_Message():
    recv = client.recv(4096)
    print(recv)


def Client(IP,PORT):
    client.connect((IP,PORT))
    while True:
        SThread=Thread(target=sent_Message,args=(input(),))
        SThread.start()
        RThread = Thread(target=recv_Message)
        RThread.start()
        



def main():
    print("P2P-Chat V0.01")
    #IP=str(input("Enter IP : "))
    #PORT=int(input("Enter Port: ")) 
    OPTION=str(input("Server or Client: "))
    if(OPTION == "Server"):
        Server('0.0.0.0',8085)
    else :
        Client('0.0.0.0',8085)

    

if __name__ ==  "__main__":
    main()

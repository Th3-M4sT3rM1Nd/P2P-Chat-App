import socket
from threading import Thread

################################################################################
                            #Client Side
################################################################################
def C_sent_Message(TEXT,client):
    b=bytes(TEXT,'utf-8')
    client.send(b)

def C_recv_Message(client):
    recv = client.recv(4096)
    print("Server: ",recv.decode("utf-8"))


def Client(IP,PORT):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP,PORT))
    while True:
        SThread=Thread(target=C_sent_Message,args=(input(),client,))
        SThread.start()
        RThread = Thread(target=C_recv_Message,args=(client,))
        RThread.start()
        
################################################################################
                                #Server
################################################################################


def SMode(IP,PORT):
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Server Open\n")
    Server.bind((IP,PORT))
    Server.listen(5)
    while True:
        conn,addr = Server.accept()
        while True:
            RThread = Thread(target=S_recv_Message,args=(conn,))
            RThread.start()
            SThread = Thread(target=S_sent_Message,args=(input(),conn,))
            SThread.start()



def S_sent_Message(TEXT,conn):
    b=bytes(TEXT,'utf-8')
    conn.send(b)

def S_recv_Message(conn):
    data = conn.recv(4096)
    print("Client : ",data.decode("utf-8"))



###############################################################################

def main():
    print("P2P-Chat V0.01")
    IP=str(input("Enter IP : "))
    PORT=int(input("Enter Port: ")) 
    OPTION=str(input("Server or Client: "))
    if(OPTION == "Server"):
        SMode(IP,PORT)
    else :
        Client(IP,PORT)

    

if __name__ ==  "__main__":
    main()

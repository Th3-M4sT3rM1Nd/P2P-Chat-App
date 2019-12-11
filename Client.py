import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client.connect(('0.0.0.0', 8085))
#msg="I am Here"
#b = bytes(msg, 'utf-8')
#client.send(b)
#from_server = client.recv(4096)

#print(from_server)


def Client(IP,PORT)

def main():
    print("P2P-Chat V0.01")
    IP=str(input("Enter IP : "))
    PORT=int(input("Enter Port: "))
    OPTION=str(input("Server or Client: "))
    if(OPTION == "Server"):
        Server(IP,PORT)
    else :
        Client(IP,PORT)

    

if __name__ ==  "__main__":
    main()

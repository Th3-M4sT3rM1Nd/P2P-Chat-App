import socket

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Server.bind(('0.0.0.0',8085))
Server.listen(5)

while True:
    conn, addr = Server.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode("utf-8")
        print(from_client)
        msg2 = "He He He"
        b2 = bytes(msg2,'utf-8')
        conn.send(b2)
    conn.close()
    print('client disconnected')

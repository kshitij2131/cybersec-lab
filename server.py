import socket

s = socket.socket()
print("socket created")

port = 3443

s.bind(('', port))
print("socket bind successfully to the port", port)

s.listen(5)
print("socket is listening...")

while True:
    c, addr = s.accept()
    print("connection request recieved with IP address", addr[0])  
    c.send('connection request accepted'.encode())

    while True:
         op = c.recv(1024).decode()
         if op == '4':
             break
         strRec = c.recv(1024).decode()
         if op == '1':
             c.send(strRec.encode())
         elif op == '2':
             c.send((strRec.upper()).encode())
         elif op == '3':
             c.send(strRec[::-1].encode())

    c.close()

    break




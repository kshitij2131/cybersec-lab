import socket

s = socket.socket()

port = 3443

s.connect(('127.0.0.1', port))

print(s.recv(1024).decode())

while True:
        print(" ")
        print ("1. echo", " ")
        print ("2. lower to upper", " ")
        print ("3. reverse", " ")
        print ("4. exit", " ")
        print ("make your choice : ")
        op = input()
        print(" ")
        s.send(op.encode())
        if op == '4':
            break
        print("enter input string :")
        strInp = input()
        s.send(strInp.encode())
        print("output recieved from the server : ", s.recv(1024).decode(), " ")

        
# print(s.recv(1024).decode())

s.close()

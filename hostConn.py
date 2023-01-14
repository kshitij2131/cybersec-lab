import sys
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created")
except socket.error as err:
    print("[ERROR] : socket creation failed...")

port = 80

try:
    hostIp = socket.gethostbyname("iitj.ac.in")
except socket.gaierror:
    print("[ERROR] : host cannot be resolved...")
    sys.exit()


s.connect((hostIp, port))

print("socket connected to official website of IIT-J")

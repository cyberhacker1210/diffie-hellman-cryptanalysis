import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 65432
PORT2 = 65433
s.bind((HOST, PORT))
s.listen()
print("Eve listening")
conn_alice, addr = s.accept()
print(f"conexion with : {addr}")

socket_bob = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_bob.connect((HOST, PORT2))
print("I'm conecting ")
data = socket_bob.recv(1024).decode('utf-8')
g, p = data.split(',')
g = int(g)
p = int(p)
e = random.randint(2, p-2)
E = pow(g,e,p)
socket_bob.sendall(f"{E}".encode('utf-8'))
B = int(socket_bob.recv(1024).decode('utf-8'))
Kbob = pow(B,e,p)

conn_alice.sendall(f"{g},{p}".encode('utf-8'))
A = int(conn_alice.recv(1024).decode('utf-8'))
conn_alice.sendall(f"{E}".encode('utf-8'))
Kalice = pow(A,e,p)
print(Kalice,Kbob)
def cipher(text, key):
    return "".join(chr(ord(c) ^ key) for c in text)

Text = conn_alice.recv(1024).decode('utf-8')
Text = cipher(Text,Kalice)
print(Text)
Text = "Virement de 10000€"
Text = cipher(Text, Kbob)
socket_bob.sendall(Text.encode('utf-8'))
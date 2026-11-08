import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 65432
s.connect((HOST, PORT))
print("I'm conecting ")
data = s.recv(1024).decode('utf-8')
g, p = data.split(',')
g = int(g)
p = int(p)
a = random.randint(2, p-2)
A = pow(g,a,p)
s.sendall(f"{A}".encode('utf-8'))
B = int(s.recv(1024).decode('utf-8'))
K = pow(B,a,p)
print(K)
def cipher(text, key):
    return "".join(chr(ord(c) ^ key) for c in text)

Text = "Virement de 100€"
Text = cipher(Text, K)
s.sendall(Text.encode('utf-8'))
print(Text)
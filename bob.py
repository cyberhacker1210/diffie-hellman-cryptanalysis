import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 65432
s.bind((HOST, PORT))
s.listen()
print("Bob listening")
conn, addr = s.accept()
print(f"conexion with : {addr}")
g = 5
p = 10007
conn.sendall(f"{g},{p}".encode('utf-8'))
b = random.randint(2, p-2)
B = pow(g,b,p)
A = int(conn.recv(1024).decode('utf-8'))
conn.sendall(f"{B}".encode('utf-8'))
K = pow(A,b,p)
print(K)
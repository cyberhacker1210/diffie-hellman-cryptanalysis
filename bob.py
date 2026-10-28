import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 65432
s.bind((HOST, PORT))
s.listen()
print("Bob listening")
conn, addr = s.accept()
print(f"conexion with : {addr}")
conn.sendall("Hello".encode('utf-8'))
data = conn.recv(1024)
print(f"message : {data.decode('utf-8')}")
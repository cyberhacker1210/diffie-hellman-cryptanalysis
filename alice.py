import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 65432
s.connect((HOST, PORT))
print("I'm conecting brother")
data = s.recv(1024)
print(f"new message : {data.decode('utf-8')}")
s.sendall("Hi brother".encode('utf-8'))
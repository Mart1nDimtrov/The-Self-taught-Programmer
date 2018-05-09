import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8888
s.connect((host, port))
msg = s.recv(0)
s.close()
print("{}".format(msg))
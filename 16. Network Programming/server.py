import socket
import datetime

today = str(datetime.datetime.today())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8888))
s.listen(5)
while True:
	connect, adress = s.accept()
	resp = (connect.recv(1024)).strip()
	connect.send(today)
	connect.close()
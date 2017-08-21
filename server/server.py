import socket
import time

s = socket.socket()
host = '0.0.0.0'
port = 12345
s.bind((host, port))

s.listen()
while True:
    c, addr = s.accept()
    c.send("connected".encode())
    data = c.recv(2048).decode()
    localtime = time.asctime(time.localtime(time.time()))
    print("At {} %s says: addr: %s port:%d".format(localtime) % (data, addr[0], addr[1]))
    c.close()
    time.sleep(60)

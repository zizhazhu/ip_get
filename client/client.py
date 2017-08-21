import socket
import time
import random

host = '127.0.0.1'
port = 12345

while True:
    s = socket.socket()
    s.connect((host, port))
    connect = s.recv(2048).decode()
    if connect == 'connected':
        s.send('pi'.encode())
    s.close()
    time.sleep(1800 + random.randint(10, 100))

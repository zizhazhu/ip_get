import socket
import time
import random

name = 'test'
beat_gap = 3600

host = '127.0.0.1'
port = 12345

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = name.encode()
    udp_client.sendto(data, (host, port))
    time.sleep(beat_gap + random.randint(10, 100))

udp_client.close()

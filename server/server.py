import socket
import time

buffsize = 1024

host = '0.0.0.0'
port = 12345

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind((host, port))

while True:
    try:
        print('Waiting for heart beats...')
        data, addr = udp_server.recvfrom(buffsize)
        data = data.decode()
        print("At {} {} says: addr: {} port:{}".format(time.ctime(), data, addr[0], addr[1]))
    except Exception:
        break

udp_server.close()

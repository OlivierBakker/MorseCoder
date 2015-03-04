import socket
import Coder

class Client():

    def __init__(self, ip='192.168.2.38', port=5005, buffer_size=1024,):

        self.tcp_ip = ip
        self.tcp_port = port
        self.buffer_size = buffer_size
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        self.socket.close()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.tcp_ip, self.tcp_port))

    def send(self, message):
        response = self.socket.send(message)
        return response

    def recieve(self):
        data = self.socket.recv(self.buffer_size)
        return data

    def close(self):
        self.socket.close()


c = Client()
c.connect()
msg = ['... --- ...', '... --- ...']
mc = Coder.MorseCode(morse_code=msg)
print(c.send(mc.__bytes__()))


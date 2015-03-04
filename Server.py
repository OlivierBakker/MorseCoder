import socket

class Server():

    def __init__(self, ip='192.168.2.38', port=5005, buffer_size=1024):
        self.ip = ip
        self.port = port
        self.buffer_size = buffer_size
        self.socket = None
        self.conn = None

    def bind_ip(self):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))

    def close_conn(self):
        self.conn.send('acknowlidged')
        self.conn.close()

    def listen(self):

        while True:

            self.socket.listen(1)
            self.conn, addr = self.socket.accept()
            print('Connection address:', addr)

            while True:
                data = self.conn.recv(self.buffer_size)
                if not data:
                    break

                print("received data:", data)
                #conn.send(data)  # echo


if __name__ == '__main__':

    s = Server()
    s.bind_ip()
    s.listen()

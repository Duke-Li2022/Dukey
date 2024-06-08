import socket
import threading


class SocketConnect:
    def __init__(self):
        self.connected_socket = None

        self.t_socket = None
        self.stop_loop = False
        self.send_message = None
        self.got_message = []

        self.com_num = -1

    def receive_loop(self):
        while not self.stop_loop:
            try:
                data = str(self.connected_socket.recv(1024).decode()).split("\r")
                for i in data:
                    x = i.split("\n")
                    for j in x:
                        if j != "":
                            self.got_message.append(j)
                # print(self.got_message)
            except TimeoutError:
                pass

    def send(self, message):
        message = str(message) + "\n"
        self.connected_socket.sendall(message.encode())

    def read(self):
        if len(self.got_message) > 0:
            message = self.got_message[0]
            del self.got_message[0]
            return message
        else:
            return None

    def start(self, connected_socket):
        self.connected_socket = connected_socket

        self.t_socket = threading.Thread(target=self.receive_loop, args=())
        self.t_socket.daemon = True
        self.t_socket.start()

    def stop(self):
        self.stop_loop = True

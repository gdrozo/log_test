import threading

class connetion:
    def __init__(self, socket, addr) -> None:
        self.addr = addr
        self.socket = socket
        self.resp = None

    def send(self, message):
        self.socket.send(message, self.addr)

    def recv(self):
        lock = threading.Lock()
        lock.acquire()
        return self.socket.recv(self.addr, lock)

    def close(self):
        self.socket.close()
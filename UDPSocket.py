import socket as sc
import threading
from time import sleep
from Connetion import connetion

AF_INET = 'A'
SOCK_DGRAM = 'B'
p = 54758

def socket(A, B):
    return individualSocket()

def gethostname():
    return sc.gethostname()

def gethostbyname(name):
    return sc.gethostbyname(name)

def getAnIp():
    global p
    p += 1
    return p

class individualSocket:
    
    def __init__(self) -> None:

        self.PACKET = 1024
        self.server_socket = sc.socket(sc.AF_INET,sc.SOCK_DGRAM)
        self.clients = 0
        self.connetions = []
        self.cWaiting = {}
        self.lock = threading.Lock()
        self.waitting = threading.Lock()
        #self.waitting.acquire()
        self.isWaitting = False
        self.t = threading.Thread(target=self.activeListen)
        self.pLock = threading.Lock()
        self.messages = {}
        self.open = True
        self.t.start()

    def activeListen(self):
        while self.open:
            if len(self.cWaiting) > 0 or self.isWaitting:
                # # print('someone is waiting')
                #self.lock.acquire()
                m, addr = self.server_socket.recvfrom(self.PACKET)
                # print('Message',m.decode(encoding='ascii', errors='ignore'),'recive from', addr)
                #self.lock.release()
                t = str(addr[0]) + str(addr[1])
                if not self.isWaitting: 
                    lock = self.cWaiting[t]
                    del self.cWaiting[t]
                    self.messages[t] = m
                    # print('returning a message')
                    lock.release()
                else:
                    # print('Accepting a guest')
                    self.addr = addr
                    self.isWaitting = False
                    # print('Releasing the waiting lock')
                    self.waitting.release()
                    #self.waitting.acquire()
                    

    def bind(self, info):
        self.server_socket.bind(info) 

    def listen(self, cs):
        self.clients = cs

    def connect(self, addr):
        self.pLock.acquire()
        port = getAnIp()
        self.pLock.release()
        host = gethostname()
        host = gethostbyname(host + ".local")
        self.bind((host, port))
        self.server_socket.sendto(('Buenas compadre').encode(encoding='ascii', errors='ignore'), addr)
        c = connetion(self, addr)
        return c

    def accept(self):
        self.isWaitting = True
        # print('waiting for a guest')
        self.waitting.acquire()
        # print('First lock')
        self.waitting.acquire()
        self.waitting.release()
        # print('Guest was been accepted')
        # print(self.addr)
        c = connetion(self, self.addr)
        self.connetions.append(c)
        return c, self.addr

    def send(self, message, addr):
        # print('trying to send', message, 'to', addr)
        self.lock.acquire()
        self.server_socket.sendto(message, addr)
        self.lock.release()
    
    def recv(self, addr, lock):
        t = str(addr[0]) + str(addr[1])
        self.cWaiting[t] = lock
        # print('waiting for a message')
        #Blocking 
        lock.acquire()
        # print('Message received')
        r = self.messages[t]
        del self.messages[t]
        return r

    def close(self):
        if len(self.cWaiting) > 0 or self.isWaitting:
            print('Trying to close the socket while waiting for a message or a guest')
            # self.open = False
            # self.server_socket.close()
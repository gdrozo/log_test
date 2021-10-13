import threading

def rrre():
    l = threading.Lock()
    l.acquire()
    #l.acquire()
    print('cacofony')

t = threading.Thread(target=rrre)
t.start()
t.join()

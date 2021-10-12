import threading
import pyshark
import subprocess
from pyshark.capture.capture import Capture

i= 0
total_length = 0

def capture(INTERFACE, PORT):
    global i
    global total_length

    capture = pyshark.LiveCapture(interface=INTERFACE)
    for raw_packet in capture.sniff_continuously():

        # filter only UDP packet
        if hasattr(raw_packet, 'udp') and raw_packet[raw_packet.transport_layer].srcport == PORT:
            i += 1
            total_length += raw_packet.udp.length
            # print('package-', i, ' size:'+length)

def getResults():
    return i, total_length

def sniff(INTERFACE, PORT):
    thread = threading.Thread(target= capture, args=(INTERFACE, PORT))
    thread.start()

def killAll():
    subprocess.run(["sudo kill tshark", ""])
    
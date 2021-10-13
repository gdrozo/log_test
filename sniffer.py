import threading
import time
import pyshark
import subprocess
from pyshark.capture.capture import Capture

DEV = False

i= 0
total_length = 0
running = True

def capturePackages(INTERFACE, PORT):
    if not DEV:
        global i
        global total_length
        global capture

        capture = pyshark.LiveCapture(interface=INTERFACE)
        try:
            for raw_packet in capture.sniff_continuously():
                if not running:
                    break
                # filter only UDP packet
                if hasattr(raw_packet, 'udp') and raw_packet[raw_packet.transport_layer].srcport == PORT:
                    i += 1
                    total_length += raw_packet.udp.length
                    # print('package-', i, ' size:'+length)
        except: 
            pass

def getResults():
    return i, total_length

def sniff(INTERFACE, PORT):
    if not DEV:
        thread = threading.Thread(target= capturePackages, args=(INTERFACE, PORT))
        thread.start()

def killAll():
    if not DEV:
        global runnings
        running = False
        subprocess.call(['sudo',  'killall', 'tshark'])

    
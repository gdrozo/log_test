import pyshark


INTERFACE = 'ens33'
PORT = '1234' 

capture = pyshark.LiveCapture(interface=INTERFACE)
for raw_packet in capture.sniff_continuously():

    i = 0
    # filter only UDP packet
    if hasattr(raw_packet, 'udp') and raw_packet[raw_packet.transport_layer].srcport == PORT:
        i += 1
        # Get the details for the packets by accessing
        # _all_fields and _all_fields.values()
        length = raw_packet.udp.length
        print('package-', i, ' size:'+length)

        # if you need to access the packet data you need to do this,
        # but it might come back in hex, which will need to be decoded. 
        # if "DATA" in str(packet.layers):
        #   print(packet.data.data)
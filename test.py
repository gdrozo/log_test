import pyshark


INTERFACE = 'ens33'
PORT = '1234' 

capture = pyshark.LiveCapture(interface=INTERFACE)
for raw_packet in capture.sniff_continuously():

   # filter only UDP packet
   #if hasattr(raw_packet, 'udp') and raw_packet[raw_packet.transport_layer].srcport == PORT:
    if True:
     # Get the details for the packets by accessing
     # _all_fields and _all_fields.values()
     field_names = raw_packet.udp._all_fields
     field_values = raw_packet.udp._all_fields.values()
     for field_name in field_names:
        for field_value in field_values:
           # you can add another filter here to get your 
           # lat & long coordinates 
           print(f'{field_name} -- {field_value}')

     # if you need to access the packet data you need to do this,
     # but it might come back in hex, which will need to be decoded. 
     # if "DATA" in str(packet.layers):
     #   print(packet.data.data)
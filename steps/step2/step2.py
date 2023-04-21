from scapy.all import *

frames=rdpcap("ping6-display.pcapng")

cpt=0
for frame in frames:
    cpt+=1
print(cpt)
# frame_choice = input("")
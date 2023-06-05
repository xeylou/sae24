#! /usr/bin/env python3

from collections import Counter
from scapy.all import sniff

## Create a Packet Counter
packet_counts = Counter()

## Define our Custom Action function
def custom_action(packet):
    # Create tuple of Src/Dst in sorted order
    key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packet_counts.update([key])
    return f"Packet #{sum(packet_counts.values())}: {packet[0][1].src} ==> {packet[0][1].dst}"

## Setup sniff, filtering for IP traffic
sniff(prn=custom_action)
#sniff(filter="host 172.16.18.69 and tcp port 80",prn = comp_pkt,count = 1)


## Print out packet count per A <--> Z address pair
print("\n".join(f"{f'{key[0]} <--> {key[1]}'}: {count}" for key, count in packet_counts.items()))

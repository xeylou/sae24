## sniffing frames containing ipv4 ##

from scapy.all import *

def print_icmpv4(frame):
    print(frame.summary())
    if frame[0][0].type == 2048:
        print(f"{frame[0].src}")
        print(f"{frame[0].dst}")
        print(f"{frame[1].src}")
        print(f"{frame[1].dst}")


nic=conf.iface
print(f"sniffing on {nic}")
sniff(filter="ip", prn=print_icmpv4, store=0, iface=nic, count=6)
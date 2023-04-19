# send frames or packets
from scapy.all import *
packet = IP(dst="172.16.5.4")/ICMP()
# send(packet)
# send(packet, ifcae="eth0")
# sr(packet)  # wait the reply
ok,nonok = srloop(packet, count=10, inter=1)

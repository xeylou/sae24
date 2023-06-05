from scapy.all import *

def action(trame):
    try:
        #la trame contient du icmpv4
        trame[ICMP].show
        print(f"====================")
        if trame[ICMP].type==8:
            print(f"C'est requête est une echo-request de {trame[IP].src} à {trame[IP].dst}")
        elif trame[ICMP].type==0:
            print(f"C'est un echo-reply de {trame[IP].src} à {trame[IP].dst}")
    except:
        exit

sniff(prn=action)
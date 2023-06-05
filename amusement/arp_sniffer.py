from scapy.all import *

def action(trame):
    try:
        #la trame contient du arp
        trame[ARP].show
        print(f"====================")
        print(f"L'@MAC source est {trame[ARP].hwsrc}")
        print(f"L'@IP source est {trame[ARP].psrc}")
        if trame[ARP].op==1:
            print(f"L'équipement demande 'who-has' ou 'qui a' l'adresse IP {trame[ARP].pdst} à l'@MAC {trame[ARP].hwdst} (en broadcast)")
        elif trame[ARP].op==2:
            print(f"L'appareil répond à une demande avec 'is-at' ou 'est à' en mettant son @MAC {trame[ARP].hwsrc}")
    except:
        exit
sniff(prn=action)
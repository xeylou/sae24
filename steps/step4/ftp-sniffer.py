from scapy.all import *

def ftp_sniffer(frame):
    try:
        tmp = frame['Raw'].load.decode('utf-8')
    except:
        pass
    if "USER" in frame['Raw'].load.decode('utf-8'):
    # if "USER" in tmp:
        # frame['Raw'].show()
        user = frame['Raw'].load.decode('utf-8').split('USER ')[1].split('\r\n')[0]
    elif "PASS" in frame['Raw'].load.decode('utf-8'):
    # elif "PASS" in tmp:
        # frame['Raw'].show()
        password = frame['Raw'].load.decode('utf-8').split('PASS ')[1].split('\r\n')[0]

nic=conf.iface
print(f"Starting sniffing on {nic}\n")
# sniff(filter="ip6 proto 58", prn=ftp_sniffer, store=0, iface=nic, count=6)
sniff(prn=ftp_sniffer, iface=nic)
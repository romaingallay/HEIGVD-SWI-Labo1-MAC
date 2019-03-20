#!/usr/bin/env python2
# SWI: Labo1 ex1
# Silvestri Romain & Gallay Romain

import sys
from scapy.all import *

def PacketHandler(pkt) :
	# To be sure it's a wifi packet
	if pkt.haslayer(Dot11ProbeReq):
		# If the packet has the required address, print it
		if pkt.addr2 == sys.argv[1]:
			print "Probe Found: " + pkt.addr2 + "  "+ pkt.info
				
# Sniff the interface wlan0
sniff(iface = "wlan0", prn = PacketHandler)

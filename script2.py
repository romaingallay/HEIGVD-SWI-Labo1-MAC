#!/usr/bin/env python2
# SWI: Labo1 ex2
# Silvestri Romain & Gallay Romain

from scapy.all import *
import sys
import requests
import json
import codecs

clients = dict()

# return the interface vendor using macvendors.co api
def Vendor(mac_address) :
	# API base URL
	url = "http://macvendors.co/api/"

	response = requests.get(url+mac_address).json()
	vendor = ""
	try :
		vendor = response['result']['company']
	except:
		vendor = "unkown"
	return vendor

# a class representing a client sending probe requests
class Client:
	def __init__(self, mac, ssid):
		self.mac = mac
		self.SSIDs = [ssid]
		self.vendor = Vendor(mac)

	def __str__(self):
		return self.mac + "(" + self.vendor + ")" + " - " + str(self.SSIDs)

	def addSSID(self, id):
		if id not in self.SSIDs:
			self.SSIDs.append(id)

def PacketHandler(pkt) :
	# to be sure it's a wifi packet
	if pkt.haslayer(Dot11) :
		# a probe request has a type == 0 and subtype == 4
		if pkt.type == 0 and pkt.subtype == 4 and pkt.info :
			mac = pkt.addr2
			# if it's the first time we see this mac address, create a client and add it to the list
			if mac not in clients:
				c = Client(mac, pkt.info)
				clients[mac] = c
				print(c)
			# else if the client has not already sent a probe request with that SSID, add SSID to the SSID array
			elif pkt.info not in clients[mac].SSIDs:
				c = clients[mac]
				c.addSSID(pkt.info)
				print(c)

# sniff the interface wlan0
sniff(iface="wlan0", prn = PacketHandler)
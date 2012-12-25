#!/usr/bin/env python
from socket import *
from select import select
import sys

HOST = raw_input('your ip: ')
SERV = raw_input('your serv (hint: if at school (Room 307), enter 192.168.100.15): ')
USER = raw_input('your user: ')


def run():

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
			elif s == sys.stdin:
				sender.sendto(sys.stdin.readline(),(SERV,6667))
	sender.close;receiver.close()
if __name__ == '__main__':
	run()

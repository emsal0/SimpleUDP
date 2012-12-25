#!/usr/bin/python

import socket, random


def run():
	serv=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	SERV = raw_input("your ip : ")
	serv.bind((SERV,6667))

	people={}
	while 1:
		data,addr=serv.recvfrom(65536)

		if addr[0] not in people.keys():
			if data not in people.values():
				people[addr[0]] = data
			else:
				people[addr[0]] = data + "_"
			continue
		print addr,": ",data
		for i in people:
			serv.sendto(people[addr[0]]+": "+data,(i,6668))
	serv.close()
if __name__ == "__main__":
	run()

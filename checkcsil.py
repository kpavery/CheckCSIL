## Check CSIL
##
## By Keith Avery
## Copyright 2013, All Rights reserved

import paramiko
import socket
import sys

workstations = ["snarf", "homer", "dilbert", "thundarr", "dudley", "cartman", "linus", "megatron", "marge", "whiley", "lupin", "elroy", "garfield", "bart", "butthead", "kyle", "scooby", "dagwood", "yogi", "mickey", "boris", "beavis", "popeye", "calvin", "aeonflux", "tygra", "taz", "pinky", "kenny", "snoopy", "dot", "speed", "akira", "tick", "optimus", "blondie", "tom", "booboo", "bugs", "eeyore", "bullwinkle", "brain", "sylvester", "racerx", "lisa", "hobbes", "wacko", "shaggy"]
workstations.sort()

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.RejectPolicy())

try:
	for workstation in workstations:
		try:
			hostname = workstation + ".cs.ucsb.edu"
			sys.stdout.write(".")
			
			client.connect(hostname=hostname,timeout=2)
			stdin, stdout, stderr = client.exec_command("who")
			lines = stdout.readlines()
			client.close()
			
			if len(lines) <= 1:
				print
				sys.stdout.write(hostname)
				break
			
		except socket.timeout:
			sys.stdout.write("T")
	
	print
except Exception, e:
	print "Exception: " + str(e)
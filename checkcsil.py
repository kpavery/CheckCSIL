## Check CSIL
##
## By Keith Avery
## Copyright 2013-2014, All Rights reserved

from paramiko import SSHClient, RejectPolicy
from socket import timeout
from sys import stdout, argv
from random import shuffle

workstations = ["snarf", "homer", "dilbert", "thundarr", "dudley", "cartman", "linus", "megatron", "marge", "whiley", "lupin", "elroy", "garfield", "bart", "butthead", "kyle", "scooby", "dagwood", "yogi", "mickey", "boris", "beavis", "popeye", "calvin", "aeonflux", "tygra", "taz", "pinky", "kenny", "snoopy", "dot", "speed", "akira", "tick", "optimus", "blondie", "tom", "booboo", "bugs", "eeyore", "bullwinkle", "brain", "sylvester", "racerx", "lisa", "hobbes", "wacko", "shaggy"]
#workstations.sort()
shuffle(workstations)

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(RejectPolicy())

username = None
if len(argv) > 1:
	username = argv[1]

try:
	for workstation in workstations:
		try:
			hostname = workstation + ".cs.ucsb.edu"
			stdout.write(".")
			
			client.connect(hostname=hostname,username=username, timeout=2)
			sshin, sshout, ssherr = client.exec_command("who")
			lines = sshout.readlines()
			client.close()
			
			if len(lines) <= 1:
				print
				stdout.write(hostname)
				break
			
		except timeout:
			stdout.write("T")
	
	print
except Exception, e:
	print "Exception: " + str(e)
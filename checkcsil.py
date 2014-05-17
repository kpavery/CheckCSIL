## Check CSIL
##
## By Keith Avery
## Copyright 2013-2014, All Rights reserved

from paramiko import SSHClient, RejectPolicy
from socket import timeout
from sys import stdout, argv, exit
from random import shuffle

workstations = ["snarf", "homer", "dilbert", "thundarr", "dudley", "cartman", "linus", "megatron", "marge", "whiley", "lupin", "elroy", "garfield", "bart", "butthead", "kyle", "scooby", "dagwood", "yogi", "mickey", "boris", "beavis", "popeye", "calvin", "aeonflux", "tygra", "taz", "pinky", "kenny", "snoopy", "dot", "speed", "akira", "tick", "optimus", "blondie", "tom", "booboo", "bugs", "eeyore", "bullwinkle", "brain", "sylvester", "racerx", "lisa", "hobbes", "wacko", "shaggy"]
padlength = max(len(x) for x in workstations)
#workstations.sort()
shuffle(workstations)

def padding(workstation):
	return " " * (padlength - len(workstation))

username = None
verbose = False
if len(argv) > 1:
	if (argv[1] == "-v" or argv[1] == "-V"):
		verbose = True
		if (len(argv) > 2):
			username = argv[2]
	elif (argv[1] == "-h" or argv[1] == "-H" or argv[1] == "help"):
		print "CheckCSIL Script"
		print "Run with -v flag to get verbose output:"
		print "  python checkcsil.py -v"
		print "To specify a username, pass the username as the last argument:"
		print "  python checkcsil.py username"
		print "Options can be combined:"
		print "  python checkcsil.py -v username"
		exit()
	else:
		username = argv[1]

try:
	for workstation in workstations:
		try:
			hostname = workstation + ".cs.ucsb.edu"
			if (not verbose):
				stdout.write(".")
				stdout.flush()
			
			client = SSHClient()
			client.load_system_host_keys()
			client.set_missing_host_key_policy(RejectPolicy())
			client.connect(hostname=hostname,username=username, timeout=2, look_for_keys=False)
			sshin, sshout, ssherr = client.exec_command("who")
			lines = sshout.readlines()
			client.close()
			
			if len(lines) <= 0:
				if (not verbose):
					print
					print hostname
				else:
					print hostname + padding(workstation) + " - no users logged in"
				break
			elif (verbose):
				print hostname + padding(workstation) + " - " + str(len(lines)) + " user" + ("s" if len(lines) != 1 else "")
			
		except timeout:
			if (not verbose):
				stdout.write("T")
				stdout.flush()
			else:
				print hostname + padding(workstation) + " - timed out"
	
except KeyboardInterrupt:
	print

except Exception, e:
	print "Exception: " + str(e)
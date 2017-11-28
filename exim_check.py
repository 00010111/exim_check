#!/usr/bin/env python

import smtplib, getopt, sys, time, socket, ssl


domain = '' # -d --domain <domain>
smtps = False # -s --smtps
ports = '25,587' # -p --port <port,port,...>
smtps_ports = '465' # -a --portsmtps <port,port,...>
verbose = False # -v --verbose
timeout = 10 # -t --timeout <SECONDS>

def usage():
	print "Usage: "
	print "-d, --domain <DOMAIN> \n\tThe Domain or IP you want to check. Mandatory to provide one domain or IP"
	print "-s, --smtps \n\tEnable check for SMTPS. DEFAULT: No check for SMTPS"
	print "-p, --port <PORTNUMBER,...>\n\tComma-separated list of port for SMTP. DEFAULT: 25,587"
	print "-a, --portsmtps <PROTNUMBER,...>\n\tComma-separated list of port for SMTPS. DEFAULT: 465"
	print "-v, --verbose \n\tenable verbose output. DEFAULT: non verbose output"
	print "-t, --timeout <SECONDS>\n\tTimeout for Socket Connection in seconds DEFAULT: 10"
	print "Examples:"
	print "\t exim_check.py -d 127.0.0.1 \t\t\t#checks localhost SMTP on port 25,587"
	print "\t exim_check.py -d 127.0.0.1 -v \t\t\t#checks localhost SMTP on port 25,587 with verbose output"
	print "\t exim_check.py -d 127.0.0.1 -s \t\t\t#checks localhost SMTP on port 25,587 & SMTPS 465"
	print "\t exim_check.py -d 127.0.0.1 -s -p 33 -a 45 \t#checks localhost SMTP on port 33 & SMTPS 45"


def banner():
	print "Tool checks for EXIM mail servers vulnerable to CVE-2017-16943, CVE-2017-16944 by checking the exim Version\nand the returned capabilities. If the mail server does not reply with a vulnerable exim version in the banner\n or does not return CHUNKING as a capability the server is assumed to be not vulnerable. Keep this in mind\nwhen testing and understanding results\nVulnerable EXIM Version:\n\t\tExim 4.89\n\t\tExim 4.88\n\nKeep in mind: A fool with a tool is still a fool.\n\nContact author on twitter: @b00010111\n"	

banner()

try:
	opts, args = getopt.getopt(sys.argv[1:],"vhsd:p:a:t:",["domain=","port=","smtpsports=","smtps","verbose","timeout="])

except getopt.GetoptError as err:
	print(err)
	exit(1)

if len(opts) == 0:
	usage()
	exit(1)

for opt, arg in opts:
	if opt in ("-s", "--smtps"):
		smtps = True
	elif opt in ("-d", "--domain"):
		domain = arg
	elif opt in ("-p","--port"):
		ports = arg
	elif opt in ("-a","--smtpsports"):
		smtps_ports = arg
	elif opt in ("-t","--timeout"):
		timeout = int(arg)
	elif opt in ("-v","--verbose"):
		verbose = True
	elif opt in ("-h","--help"):
		usage()
		exit(0)
	else: 
		usage()
		assert False, "unhandled option"

if len(domain) == 0:
	usage()
	exit(1)

port_array = ports.split(",")

for p in port_array:

	print("Figuring out if " + domain + " on port: " + p + " is a Exim Server Version 4.88 or 4.89")
	try:
		s = socket.socket()
		s.settimeout(timeout)
		s.connect((domain,int(p)))
		banner = s.recv(1024)
		if verbose:
			print banner	
		if "Exim 4.89" in banner or "Exim 4.88" in banner:
			print "Found a banner coutaining a vulnerable exim version"
			if verbose:
				print banner

			print ("SMTP Testing: " + domain + " on port: " + p)
			server = smtplib.SMTP(domain,p)
			server.ehlo()
			ehlo_result = server.ehlo_resp
			if verbose:
				print ehlo_result
			if "CHUNKING" in ehlo_result:
				print("\n#############################")
				print("Found vulnerable EXIM Version and chunking enabled for " + domain + " on port: " + p)
				if verbose:
					print(ehlo_result)
				print("You should consider disabling chunking unless are not able to update" ) 
				print("#############################")
			else:
				print("Domain " + domain + " on port: " + p + " seems not to be vulnerable as CHUNKING is not enabled" )
			server.quit()
		else:
			print("Domain " + domain + " on port: " + p + " seems not to be a vulnerable EXIM version" )

		s.close()
	except Exception as e:
		print("Error while testing " + domain + " on port: " + p + " - you are sure there connection is possible?")
		if verbose:
			print e

	print("waiting 2 seconds")
	time.sleep(2)

if smtps:
	print("Testing SMPTS")
	ports_array = smtps_ports.split(",")

	for ps in ports_array:

		print("Figuring out if " + domain + " on port: " + ps + " is a Exim Server Version 4.88 or 4.89")
		try:	
			s = socket.socket()
			s.settimeout(timeout)
			ws = ssl.wrap_socket(s)
			ws.connect((domain,int(ps)))
			banner = ws.recv(1024)
			if verbose:
				print banner
			if "Exim 4.89" in banner or "Exim 4.88" in banner:
			
				print "Found a banner coutaining a vulnerable exim version"
				if verbose:
					print banner
			
				print ("SMTPS Testing: " + domain + " on port: " + ps)
				servers = smtplib.SMTP_SSL(domain,ps)
				servers.ehlo()
				ehlo_result = server.ehlo_resp
				if verbose:
					print ehlo_result
				if "CHUNKING" in ehlo_result:
					print("\n#############################")
					print("Found vulnerable EXIM Version and chunking enabled for " + domain + " on port: " + p)
					if verbose:
						print(ehlo_result)
					print("You should consider disabling chunking unless are not able to update" ) 
					print("#############################")
				else:
					print("Domain " + domain + " on port: " + ps + " seems not to be vulnerable as CHUNKING is not enabled" )
		
				servers.quit()
			else:
				print("Domain " + domain + " on port: " + p + " seems not to be a vulnerable EXIM version" )
			s.close()

		except Exception as e:
			print("Error while testing " + domain + " on port: " + ps + " - you are sure there connection is possible?")
			if verbose:
				print e

		print("waiting 2 seconds")
		time.sleep(2)


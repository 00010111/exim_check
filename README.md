# exim_check

Tool checks for EXIM mail servers vulnerable to CVE-2017-16943, CVE-2017-16944 by checking the exim Version
and the returned capabilities. If the mail server does not reply with a vulnerable exim version in the banner
or does not return CHUNKING as a capability the server is assumed to be not vulnerable. Keep this in mind 
when testing and understanding results.
Vulnerable EXIM Version:
    Exim 4.89
    Exim 4.88


This is neither rocket science nor in any kind advance, it simply does a bit of banner grabbing and string comparison. But it is a nice little finger excercise.

Keep in mind: A fool with a tool is still a fool.
Contact author on twitter: @b00010111



Usage: 
-d, --domain <DOMAIN> 
	The Domain or IP you want to check. Mandatory to provide one domain or IP
-s, --smtps 
	Enable check for SMTPS. DEFAULT: No check for SMTPS
-p, --port <PORTNUMBER,...>
	Comma-separated list of port for SMTP. DEFAULT: 25,587
-a, --portsmtps <PROTNUMBER,...>
	Comma-separated list of port for SMTPS. DEFAULT: 465
-v, --verbose 
	enable verbose output. DEFAULT: non verbose output
-t, --timeout <SECONDS>
	Timeout for Socket Connection in seconds DEFAULT: 10
Examples:
	 exim_check.py -d 127.0.0.1 			#checks localhost SMTP on port 25,587
	 exim_check.py -d 127.0.0.1 -v 			#checks localhost SMTP on port 25,587 with verbose output
	 exim_check.py -d 127.0.0.1 -s 			#checks localhost SMTP on port 25,587 & SMTPS 465
	 exim_check.py -d 127.0.0.1 -s -p 33 -a 45 	#checks localhost SMTP on port 33 & SMTPS 45


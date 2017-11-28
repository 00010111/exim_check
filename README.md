# exim_check

Tool checks for EXIM mail servers vulnerable to CVE-2017-16943, CVE-2017-16944 by checking the exim Version
and the returned capabilities. If the mail server does not reply with a vulnerable exim version in the banner
or does not return CHUNKING as a capability the server is assumed to be not vulnerable. Keep this in mind 
when testing and understanding results.<br/>
Vulnerable EXIM Version:<br/>
    Exim 4.89<br/>
    Exim 4.88<br/>


This is neither rocket science nor in any kind advance, it simply does a bit of banner grabbing and string comparison. But it is a nice little finger excercise.<br/>

Keep in mind: A fool with a tool is still a fool.<br/>
Contact author on twitter: @b00010111<br/>


<pre>
Usage: 
-d, --domain <DOMAIN><br/> 
	The Domain or IP you want to check. Mandatory to provide one domain or IP<br/>
-s, --smtps <br/>
	Enable check for SMTPS. DEFAULT: No check for SMTPS<br/>
-p, --port <PORTNUMBER,...><br/>
	Comma-separated list of port for SMTP. DEFAULT: 25,587<br/>
-a, --portsmtps <PROTNUMBER,...><br/>
	Comma-separated list of port for SMTPS. DEFAULT: 465<br/>
-v, --verbose <br/>
	enable verbose output. DEFAULT: non verbose output<br/>
-t, --timeout <SECONDS><br/>
	Timeout for Socket Connection in seconds DEFAULT: 10<br/>
Examples:<br/>
	 exim_check.py -d 127.0.0.1 			#checks localhost SMTP on port 25,587<br/>
	 exim_check.py -d 127.0.0.1 -v 			#checks localhost SMTP on port 25,587 with verbose output<br/>
	 exim_check.py -d 127.0.0.1 -s 			#checks localhost SMTP on port 25,587 & SMTPS 465<br/>
	 exim_check.py -d 127.0.0.1 -s -p 33 -a 45 	#checks localhost SMTP on port 33 & SMTPS 45<br/>
</pre>

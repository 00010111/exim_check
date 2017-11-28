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


# exim_check

"Tool checks for EXIM mailservers vulnerable to CVE-2017-16943, CVE-2017-16944 by checking the exim Version
and the returned capabilites. If the mailserver does not reply with a vulnerable exim version in the banner
or does not return CHUNKING as a capability the server is assumed to be not vulnerable. Keep this in mind 
when testing and understanding results.
Vulnerable EXIM Version:
    Exim 4.89
    Exim 4.88

Keep in mind: A fool with a tool is still a fool.
Contact author on twitter: @b00010111

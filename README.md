# dnstressor

This is a Python3 script to stress test (and possibly DOS) your DNS server with DNS queries for A records of random hostnames.

The script doesn't take any arguments and simply uses your OS configured DNS server as the target (as per /etc/resolv.conf for example).

It runs forever, use "Ctrl C" (repeatedly) to kill it.

Please be sensible and only use it on authorized target servers.

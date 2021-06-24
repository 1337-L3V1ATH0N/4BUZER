#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
atobm $filepath 2>&1 | awk -F "'" '{printf "%s",$2}'

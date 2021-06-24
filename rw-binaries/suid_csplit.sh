#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
csplit $filepath 1
cat xx01

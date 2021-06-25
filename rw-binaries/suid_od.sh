#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
od -An -c -w9999 "$filepath"

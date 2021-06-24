#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
iconv -f 8859_1 -t 8859_1 "$filepath"

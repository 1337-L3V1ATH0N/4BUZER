#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
unexpand -t99999999 "$filepath"

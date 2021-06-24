#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
fold -w99999999 "$filepath"

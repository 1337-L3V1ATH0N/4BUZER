#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
hexdump -C "$filepath"

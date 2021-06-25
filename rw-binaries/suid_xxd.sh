#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
xxd "$filepath" | xxd -r

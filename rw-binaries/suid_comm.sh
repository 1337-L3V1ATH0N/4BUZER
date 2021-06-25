#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
comm $filepath /dev/null 2>/dev/null

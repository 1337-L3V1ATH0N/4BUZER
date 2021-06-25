#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
msgmerge -P $filepath /dev/null

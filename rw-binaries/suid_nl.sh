#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
nl -bn -w1 -s '' $filepath

#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
rev $filepath | rev

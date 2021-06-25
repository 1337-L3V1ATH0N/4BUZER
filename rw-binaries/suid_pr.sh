#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
pr -T $filepath

#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
run-mailcap --action=view $filepath

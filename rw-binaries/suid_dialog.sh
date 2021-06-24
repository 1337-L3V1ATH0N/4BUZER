#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
dialog --textbox "$filepath" 0 0

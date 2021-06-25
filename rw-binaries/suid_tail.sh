#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
tail -c1G "$filepath"

!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
cut -d "" -f1 "$filepath"

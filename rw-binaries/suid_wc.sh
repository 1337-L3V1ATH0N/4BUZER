#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
wc --files0-from "$filepath"

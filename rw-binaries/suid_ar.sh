#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
OUTFILE=$(mktemp -u)
ar r "$OUTFILE" "$filepath"
cat "$OUTFILE"

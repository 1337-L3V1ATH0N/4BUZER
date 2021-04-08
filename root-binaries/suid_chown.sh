#!/bin/bash

echo -en "\n[!] Files Ownership you want to change(specify full path): "
read LFILE

chown $(id -un):$(id -gn) $LFILE

echo "Ownership changed of $LFILE"

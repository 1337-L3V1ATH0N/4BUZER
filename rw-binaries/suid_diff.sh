#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
diff --line-format=%L /dev/null $filepath

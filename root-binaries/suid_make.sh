#!/bin/bash

COMMAND='/bin/sh -p'
make -s --eval=$'x:\n\t-'"$COMMAND"

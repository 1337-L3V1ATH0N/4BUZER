#!/bin/bash

echo 'hooi'

start-stop-daemon -n $RANDOM -S -x /bin/sh -- -p



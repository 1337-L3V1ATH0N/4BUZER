#!/bin/bash

run-parts --new-session --regex '^sh$' /bin --arg='-p'


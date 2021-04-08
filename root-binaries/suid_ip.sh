#!/bin/bash

ip netns add foo
ip netns exec foo /bin/sh -p
ip netns delete foo


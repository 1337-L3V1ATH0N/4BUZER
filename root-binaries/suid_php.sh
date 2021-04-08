#!/bin/bash

CMD="/bin/sh"
php -r "pcntl_exec('/bin/sh', ['-p']);"


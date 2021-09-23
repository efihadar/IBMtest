#!/bin/bash

[[ ! -z $1 ]] && for x in $(find /var/log/app/*.log -type f -mtime +$1); do tar -cvf "$x.tar.gz" "$x" && rm -f "$x" ; done || echo "please provide number of days"
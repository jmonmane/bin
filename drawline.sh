#!/bin/bash
if [[ ! $1 ]]; then
    echo " Supply Args "
elif
    [[ $2 ]]; then
    char="$2"
else
    char="="
fi
length="$1"

for (( i=0; i<$length; i++ )); do
    printf "$char"
    sleep 1
done
printf "\n"
exit 0

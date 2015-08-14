#!/bin/bash

VALUE=$(($RANDOM % 10))
GUESS=

until [[ "$GUESS" -eq "$VALUE" ]]; do
    read -p "Take a Guess" GUESS
    if [[ "$GUESS" -lt "$VALUE" ]]; then
        echo "Higher!"
    elif [[ "$GUESS" -gt "$VALUE" ]]; then
        echo "Lower!"
    else
        echo "YES!"
    fi
done
exit 0


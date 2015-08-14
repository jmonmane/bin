#!/bin/bash

while read -r; do
    printf "$REPLY"
done; < "$1"

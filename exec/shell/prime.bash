#!/bin/bash

is_prime() {
    if [ "$1" -lt 2 ]; then
        echo "False"
        return
    fi
    for ((i=2; i<$1; i++)); do
        if [ "$(($1 % $i))" -eq 0 ]; then
            echo "False"
            return
        fi
    done
    echo "True"
}

read -p "Bitte gib eine Zahl ein: " num
if [ "$(is_prime $num)" = "True" ]; then
    echo "$num ist eine Primzahl."
else
    echo "$num ist keine Primzahl."
fi

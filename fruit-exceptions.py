#!/usr/bin/env python3

fruits = ["apple", "banana", "cherry"]

for i in range(21):
    try:
        print(fruits[i])
    except IndexError:
        break
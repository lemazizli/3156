#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result
if len(sys.argv)>1:
    f = factorial(int(sys.argv[1]))
    print(f)


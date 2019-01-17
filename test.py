#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if(len(s)==1):
        return n
    letters = list(s)
    repeatedString = ''
    current = 0
    while len(repeatedString)<=n:
        repeatedString+=(letters[current])
        if(current!=(len(letters)-1)):
            current += 1
        else:
            current = 0
        # print(repeatedString)
    
    count = 0
    for letter in list(repeatedString):
        if(letter == letters[0]):
            count += 1
    return count
# a
# 1000000000000
print(repeatedString("a",1000000000000))
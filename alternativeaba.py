#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):

    distinctList = []
    countList = []
    for c in s:
        if c not in distinctList:
            distinctList.append(c)
    for d in distinctList:
        count = s.count(d)
        countList.append(count)
    #print(countList)
    countList.sort()
    key = countList[0]
    flags = 0
    for count in countList:
        if(key != count):
            print(key,count)
            if(count-key==1):
                flags+=1
            else:
                return "NO"
    if(flags > 1):
        return "NO"
    else:
        return "YES"

        
if __name__ == '__main__':
    

    s = input()

    result = isValid(s)
    print(result)

    

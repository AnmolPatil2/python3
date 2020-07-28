#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    di={}
    for i in magazine:
        if i in di:
            di[i]+=1  
        else:
            di[i]=1 
    for j in note:
        if(di[j]>0):
            di[j]-=0
        else:
            return "No"
    return "Yes"
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

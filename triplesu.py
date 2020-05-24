#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.


def triplets(a, b, c, al, bl, cl):
    t = 0
    ac = 0
    cc = 0
    aa = 0
    ca = 0
    ai = 0
    ci = 0
    re = 0
    for i in range(bl):
        if(b[i] == re):
            continue
        else:
            re = b[i]

        while(ai < al):
            if(a[ai] <= b[i]):
                #print(a[ai], end=" ")
                # print(b[i])
                ac += 1
                ai += 1
            else:

                break

        while(ci < cl):
            if(c[ci] <= b[i]):
                #print(a[ai], end=" ")
                # print(b[i])
                cc += 1
                ci += 1
            else:

                break
        print(ac)
        print(cc)
        t += ac * cc

    return(t)


if __name__ == '__main__':

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(set(list(map(int, input().rstrip().split()))))
    
    arrb = set(list(map(int, input().rstrip().split())))

    arrc = set(list(map(int, input().rstrip().split())))
    ans = triplets(arra, arrb, arrc, lena, lenb, lenc)

    print(ans)

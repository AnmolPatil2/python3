#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    l = np.zeros(n)
    for i in range(0, m):
        a, b, k = queries[i]
        a -= 1
        b -= 1
        for j in range(a, b+1):
            l[j] += k
        print(l)
    return(max(l))


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    print(int(arrayManipulation(n, queries)))

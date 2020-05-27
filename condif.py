#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.


def pairs(k, arr):
    l = set([i-k for i in arr if i-k > 0])
    arr = set(arr)
    return (l.intersection(arr))


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.


def whatFlavors(cost, money):
    l = {}
    n = len(cost)

    for i in range(n):
        x = money-cost[i]
        if(x > 0):
            if(cost[i] in l):
                print(l[cost[i]]+1, end=" ")
                print(i+1)

            else:
                l[x] = i


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

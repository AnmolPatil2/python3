#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.


def minTime(machines, goal):

    lb = machines[0]
    ub = machines[-1]

    while(lb < ub):
        key = int((lb+ub)/2)
        if(goal == key):
            return key
        elif(goal < key):
            ub = key+1
        else:
            lb = key-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = (list(map(int, input().rstrip().split())))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()

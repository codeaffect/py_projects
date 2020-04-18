#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.


def time_delta(t1, t2):
    tf = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, tf)
    t2 = datetime.strptime(t2, tf)
    return str(int(abs((t1-t2).total_seconds())))


t = int(input())

for t_itr in range(t):
    t1, t2 = input(), input()
    delta = time_delta(t1, t2)
    print(delta, sep='\n')

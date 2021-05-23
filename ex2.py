#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:01:32 2021

@author: try42
"""
file = open('2021_C_2.txt', 'r') 
 
#overwrite input to mimic google input
def input():
    line = file.readline() 
    return line



# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Kick Start problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    n=n[0]
    incre = 0
    count = 0
    while (n-(incre*(incre+1)/2))// (incre+1) >0:
        k = (n-incre*(incre+1)/2)// (incre+1)
        if k == (n-incre*(incre+1)/2)/ (incre+1):
            count = count+1
        incre = incre+1

    print("Case #{}: {}".format(i, count))
    # check out .format's specification for more formatting options

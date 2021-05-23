#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 13:01:32 2021

@author: try42
"""
file = open('2021_C_1.txt', 'r') 
 
#overwrite input to mimic google input
def input():
    line = file.readline() 
    return line
firstchar = 'a'
def prechar(ch, k):
    return chr(ord('a') + (ord(ch)-ord('a') - 1)%k)

def trivialisation (mini,k):
    n = len(mini)
    m=''
    for i in mini:
        m += chr(min(ord('a')+k, ord(i)))
    moitier =  n//2
    modulo = n%2
    trivial = m[0:moitier]
    if(modulo  == 1 ):
        trivial += m[moitier]
    trivial += m[0:moitier][::-1]
    return trivial


# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Kick Start problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
    s = str(input())
    s = s.replace('\n', '')
    count = 0
    trivial = trivialisation (s,k)
    if s > trivial :
        count = count +1
    moitier =  n//2
    modulo = n%2
    vitesse = 0
    potenciel = moitier+modulo
    for truc in s[0:potenciel][::-1]:
        count = count +(ord(truc)-ord('a'))*pow(k,vitesse )
        vitesse = vitesse+1
    print("Case #{}: {}".format(i,  count))
    # check out .format's specification for more formatting options
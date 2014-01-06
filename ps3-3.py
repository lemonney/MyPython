#Problem Set 3, Problem 3
from string import *

def subStringMatchExact(target,key):
    exactMatch = ()
    flag = 1
    idx = countSubStringMatch(target, key, 0)
    while idx != -1:
        exactMatch += (idx,)
        idx = countSubStringMatch(target, key, idx+1)
    return exactMatch

def countSubStringMatch(target, key, n):
    return str.find(target, key, n)

def constrainedMatchPair(firstMatch, secondMatch, length):
    oneSubMatch = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                oneSubMatch += (n,)
    return oneSubMatch

target = 'atgacatgcacaagtatgcat'
key1 = 'a'
key2 = 'gc'

starts1 = subStringMatchExact(target,key1)
starts2 = subStringMatchExact(target,key2)
length = key1.__len__()
print(starts1, starts2, length)
print('The satisfied tuple is', constrainedMatchPair(starts1, starts2, length))
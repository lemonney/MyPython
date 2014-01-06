#Problem Set 3, Problem 4
from string import *
def countSubStringMatch(target, key, n):
    return str.find(target, key, n)

#exact matches
def subStringMatchExact(target,key):
    exactMatch = ()
    flag = 1
    idx = countSubStringMatch(target, key, 0)
    while idx != -1:
        exactMatch += (idx,)
        idx = countSubStringMatch(target, key, idx+1)
    #print(startPoints)
    return exactMatch

#matches with up to one substitution
def constrainedMatchPair(firstMatch, secondMatch, length):
    oneSubMatch = ()
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                oneSubMatch += (n,)
    return oneSubMatch

#matches with only one substitution
def subStringMatchExactlyOneSub(target, key):
    exactOneSubMatch = ()
    exactMatch = subStringMatchExact(target, key)
    starts1 = subStringMatchExact(target,key[0])
    starts2 = subStringMatchExact(target,key[2:])
    length = 1
    oneSubMatch = constrainedMatchPair(starts1, starts2, length)
    for subPoint in oneSubMatch:
        flag = 0
        for exactpoint in exactMatch:
            if subPoint == exactpoint:
                flag = 1
                break
        if flag == 0:
            exactOneSubMatch += (subPoint,)
    return exactOneSubMatch

target = 'atgacatgcacaagtacgcaggc'
key = 'atgc'
print('The matches with only one substitution is', subStringMatchExactlyOneSub(target, key))

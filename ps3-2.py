#Problem Set 3, Problem 2
from string import *

def subStringMatchExact(target,key):
    exactMatch = ()
    flag = 1
    idx = countSubStringMatch(target, key, 0)
    while idx != -1:
        exactMatch += (idx,)
        idx = countSubStringMatch(target, key, idx+1)
    #print(startPoints)
    return exactMatch

def countSubStringMatch(target, key, n):
    return str.find(target, key, n)

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

print('The starting points of matches of "', key10, '" in "', target1, '" is ',
      subStringMatchExact(target1, key10))
print('The starting points of matches of "', key11, '" in "', target1, '" is ',
      subStringMatchExact(target1, key11))
print('The starting points of matches of "', key12, '" in "', target1, '" is ',
      subStringMatchExact(target1, key12))
print('The starting points of matches of "', key13, '" in "', target1, '" is ',
      subStringMatchExact(target1, key13))
print('The starting points of matches of "', key10, '" in "', target2, '" is ',
      subStringMatchExact(target2, key10))
print('The starting points of matches of "', key11, '" in "', target2, '" is ',
      subStringMatchExact(target2, key11))
print('The starting points of matches of "', key12, '" in "', target2, '" is ',
      subStringMatchExact(target2, key12))
print('The starting points of matches of "', key13, '" in "', target2, '" is ',
      subStringMatchExact(target2, key13))



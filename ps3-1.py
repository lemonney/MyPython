#Problem Set 3, Problem 1
from string import *
def countSubStringMatch(target,key):
    return str.find(target, key)

def countSubStringMatchRecursive (target, key):
    count = 0
    #print('target = ', target, ', key = ', key)
    idx = countSubStringMatch(target, key)
    #print('idx = ', idx)
    while  idx != -1:
        count += 1
        target = target[idx+1:]
        #print('target = ', target)
        idx = countSubStringMatch(target, key)
        #print('idx = ', idx)
    return count

target = 'atgacatgcacaagtatgcat'
key = 'atgc'
print('"', key, '" appears in "', target, '" is ',
      countSubStringMatchRecursive(target, key), 'times')

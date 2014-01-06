#Problem Set 1, Problem 1
from math import *

i = 0
number = 2
list = []
while i < 1000:
    j = 2
    while j < number:
        if number % j == 0: break
        j += 1
    if j == number:
        list = list + [number]
        i += 1
    number += 1
print('The First 1000 Primes is: ')
for n in range(100):
    print(list[n*10 : (n+1)*10])
print('The 1000th Prime is: ', list[-1])

ith = 1000
productLog = 0
for i in range(ith-1):
    #print(list[i])
    productLog += log(list[i])
print('The log of product of primes less than n is:', productLog)
print('n is: ', list[ith-1])
print('The product of primes less than n <= e**n?\n',productLog <= list[ith-1])
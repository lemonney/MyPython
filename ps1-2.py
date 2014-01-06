#Problem Set 1, Problem 2
from math import *

n = input('Please input an integer bigger than 2:')

number = 2
sumLog = 0
while number < int(n):
    j = 2
    while j < number:
        if number % j == 0: break
        j += 1
    if j == number:
        sumLog += log(number)
    number += 1

print('The sum of logarithms of primes less than n is:', sumLog)
print('n is: ', n)
print('The ratio from sum to n is:\n',sumLog/int(n))

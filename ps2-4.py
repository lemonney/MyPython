#Problem Set 2, Problem 3

x = int(input('Input the first size: '))
y = int(input('Input the second size: '))
z = int(input('Input the third size: '))

print('x =', x, ', y =', y, ', z =', z)
large = 0
for n in range(1, 200):
    flag = 0
    for c in range(int(n/z)+1):
        for b in range(int(n/y)+1):
            for a in range(int(n/x)+1):
                if x*a + y*b + z*c == n:
                    flag = 1
                    #print('The solution of ', n, ' is:', a, b, c)
    if flag == 0:
        #print('There is no solution for ', n)
        large = n

print('Given package sizes <', x, '>, <', y, '>, and <', z, '>,\n'
      'the largest number of McNuggets that cannot be bought in exact quantity: <', large, '>')


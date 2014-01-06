#Problem Set 2, Problem 1
#a = 0
#b = 0
#c = 0
#flag = 0
for n in range(50, 56):
    flag = 0
    for c in range(int(n/20)+1):
        for b in range(int(n/9)+1):
            for a in range(int(n/6)+1):
                if 6*a + 9*b + 20*c == n:
                    flag = 1
                    print('The solution of ', n, ' is:', a, b, c)
    if flag == 0:
        print('There is no solution for ', n)
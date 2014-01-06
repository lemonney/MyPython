#Problem Set 2, Problem 3
n = 1
num = 1
flag = 0
ctr = 0
while ctr < 6:
    ctr = 0
    for i in range(num, num + 6):
        flag = 0
        for c in range(int(i/20)+1):
            for b in range(int(i/9)+1):
                for a in range(int(i/6)+1):
                    if 6*a + 9*b + 20*c == i:
                        flag = 1
        if flag == 0:
            n = i
        else:
            ctr += 1
    #print(n)
    num += 1

print('Largest number of McNuggets that cannot be bought in exact quantity: <', n, '>')

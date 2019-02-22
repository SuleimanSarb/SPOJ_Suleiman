import math

t = int(input())

for i in range(t):
    n,m = map(int , input().split())
    for j in range(n , m + 1):
        s = 0 
        if j == 2:
            print(j)
        else:
            k = int(math.sqrt(j))
            for l in range(2 , k + 1):
                if j % l == 0:
                    s += 1
            if s == 0 and j != 1:
                print(j)
    print(end=' ')

n,m = map(int,input().split())
k = 0
a = list(map(int,input().split()))
for i in range(n):
    k += a[i]
    print(k//m,end=' ')
    k %= m

n = int(input())
a = list(map(int,input().split()))
a.sort()
s1 = 0
s2 = 0
for i in range(n//2):
    s1 += a[i]
for i in range(n//2,n):
    s2 += a[i]
print(s2 - s1)

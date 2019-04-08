import sys
n,m = map(int,input().split())
a = list(map(int,input().split()))
t = 0
s = 0
for i in range(n):
    if a[i] > m:
        print('no')
        sys.exit()
    s = s + a[i]
if s-n+1<m:
    print('no')
else:
    print('yes')

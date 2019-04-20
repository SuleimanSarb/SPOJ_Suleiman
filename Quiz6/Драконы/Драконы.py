s,n = map(int,input().split())
x,y = map(int,input().split())
a=dict.fromkeys([x],y)
for i in range(n-1):
    x,y = map(int,input().split())
    a.update({x:y})
k = 0
for i,j in a.items():
    if s > i:
        s += j
        k += 1
if k == n:
    print('YES')
else:
    print('NO')
    

n = int(input())
a = list(map(int,input().split()))
s=0
a.sort()
for i in range(0,n,2):
    s = s +( a[i+1]-a[i])
print(s)
    

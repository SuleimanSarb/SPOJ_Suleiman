import sys
n = int(input())
a = [1,1]
k = 0
i = 2
while(k < n):
    k = a[i-1]+a[i-2]
    if k == n:
        print('1')
        print(i+1)
        sys.exit()
    a.append(k)
    i+=1
print('0')
    

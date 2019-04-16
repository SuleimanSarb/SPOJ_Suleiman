n,m =  map(int,input().split())
a = []
k = 0
for i in range(n):
        a.append(list(map(int,input().split())))
        for j in range(0,2 * m,2):
            if a[i][j] ==1 or a[i][j+1] == 1:
                k+=1
print(k)

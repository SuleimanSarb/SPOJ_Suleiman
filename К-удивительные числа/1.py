k = int(input())
s=0;
for i in range(1,k + 1):
    j=i
    m=0
    while j>0:
      m=m*10+j % 10;
      j=j // 10
    if i+m==k:
        s=s+1
print(s)

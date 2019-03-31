n = int(input())
a = list(map(int,input().split()))
b1 = []
b2 = []
for i in range(n):
  if a[i] % 2 == 0:
    b1.append(a[i])
  else:
    b2.append(a[i])
for i in range(len(b2)):
  print(b2[i],end=' ')
print(" ")
for i in range(len(b1)):
  print(b1[i],end=' ')
print(" ")  
if len(b1) < len(b2):
  print("NO")
else:
  print("YES")

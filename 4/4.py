import math

def palindrom(num):
    l = 0
    r = len(num)
    while l < r:
        if num[l] != num[r - 1]:
            return 0
        l += 1
        r -= 1 
    return 1

t = int(input())
for i in range(t):
    number = str(input())
    number = str(int(number) + 1)
    while palindrom(number)==0:
        number = str(int(number) + 1)
    print(number)

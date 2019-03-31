k = int(input())
for i in range(k):
    a = str(input())
    h = int(int(a[3] - '0') * 100 + int(a[4] - '0') * 10 + int(a[5] - '0')) + 1
    h1 = int(int(a[3] - '0') * 100 + int(a[4] - '0') * 10 + int(a[5] - '0')) - 1
    if a[0] + a[1] + a[2]== h % 10 + '0' + h % 100 / 10 + '0' + h % 1000 / 100 + '0' or a[0] + a[1] + a[2] == h1 % 10 + '0' + h1 % 100 / 10 + '0' + h1 % 1000 / 100 + '0':
        print('Yes')
    else:
        print('No')
        

m = int(input())
while m != 0:
    p = m
    s = 0
    for i in range(m + 1):
        p = i
        while p != 0:
            if p < 10:
                if i % 2 != 0:
                    s = s + p % 10
                else:
                    s = s - p % 10
                p = p // 10
            else:
                if i % 2 == 0:
                    s = s + p % 10
                else:
                    s = s - p % 10
                p = p // 10
    print(s)
    m = int(input())

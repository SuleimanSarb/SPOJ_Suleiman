n = int(input())
while n != -1:
    l = [1]
    m = -1
    i = 1
    while m < n:
        m = l[i-1] + 6 * i
        l.append(m)
        i += 1
    if l[-1] == n:
        print("Y")
    else:
        print("N")
    n = int(input())


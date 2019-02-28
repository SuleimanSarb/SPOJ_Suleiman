p = int(input())
l = []
for i in range(p):
    ttt = 0
    tth = 0
    tht = 0
    thh = 0
    htt = 0
    hth = 0
    hht = 0
    hhh = 0
    n = int(input())
    a = input()
    for j in range(len(a)-2):
        m = a[j] + a[j+1] + a[j+2]
        if m == 'TTT':
            ttt += 1
        elif m == 'TTH':
            tth += 1
        elif m == 'THT':
            tht += 1
        elif m == 'THH':
            thh += 1
        elif m == 'HTT':
            htt += 1
        elif m == 'HTH':
            hth += 1
        elif m == 'HHT':
            hht += 1
        elif m == 'HHH':
            hhh += 1
    l.append([])
    l[n-1] = [n, ttt, tth, tht, thh, htt, hth, hht, hhh]
for i in range(p):
    print (*l[i], sep = ' ')

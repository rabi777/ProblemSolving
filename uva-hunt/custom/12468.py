c = []
d = []
while True:
    try:
        a, b = input().split()
        c.append(int(a))
        d.append(int(b))
    except:
        break
for i in range(len(c)):
    if c[i] != -1 and d[i] != -1:
        res = abs(c[i] - d[i])
        if res < 50:
            print(res)
        else:
            print(100-res)


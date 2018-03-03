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
    if d[i] > c[i]:
        print(d[i] - c[i])
    else:
        print(c[i]-d[i])

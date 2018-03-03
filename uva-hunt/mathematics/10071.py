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
    v = c[i]*d[i]
    print(2*v)

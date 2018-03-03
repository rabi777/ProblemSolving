c = []
it = []
ot = []

while True:
    try:
        a = input()
        c.append(a)

    except:
        break
for i in range(0, int(c[0])):
    lt = len(c[i + 1])
    n = int(str(len(c[i + 1]) ** (1 / 2)).split('.')[0])
    k = 0
    h = 0
    if n * n == lt:
        for j in range(n):
            k = n * (j + 1)
            it.append(c[i + 1][h:k])
            h = k
        ae = list(map(list, list(zip(*it))))
        ut = ''
        for s in range(len(ae)):
            ut += ''.join(ae[s])
        print(ut)
        it.clear()
    else:
        print("INVALID")

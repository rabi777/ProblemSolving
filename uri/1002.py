import math

c = []
while True:
    try:
        a = float(input())
        c.append(math.pi * (a ** 2))
    except:
        break

for i in c:
    print("A = {0:.4f}".format(i))

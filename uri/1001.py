
c = []
while True:
	try:
		a = int(input())
		b = int(input())
		d = a+b
		c.append(d)
		
	except:
		break
for i in c:
	print("X =", i)

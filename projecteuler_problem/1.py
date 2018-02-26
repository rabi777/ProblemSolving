a = 1
b = 0
while a != 1000:
	if a%3==0 or a%5==0:
		b+=a
		print(b)
	a+=1
print(b)
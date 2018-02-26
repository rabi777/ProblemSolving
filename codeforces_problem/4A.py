def num(w):
	if(w<=100 and w%2==0):
		if((w/2)%2==0):
			print("YES")
		else:
			print("NO")
	else:
		print("NO")

for i in range(1,101):
	w = int(input())
	num(w)
a = int(input())

for i in range(a):
	space = a-1-i
	for c in range(space):
		print(" ",end="")
	
	star = i*2+1
	for s in range(star):
		print("*",end="")
		
	print()
a = list(map(int, input().split()))

N = len(a)

for k in  range(N):
	for i in range(N-1):
		if a[i]> a[i+1] : 
			a[i], a[i+1] = a[i+1], a[i]
		
for i in range(N):	
	if i%10 == 0 or i==0:
		print(end=' ')
		
	print(f'{a[i]}',end='')
	
	if i%10 == 9 and i!=99:
		print()
	elif i==99:
		print(end='')
	else:
		print(end=' ')

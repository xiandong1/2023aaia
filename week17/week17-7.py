a=list(map(int,input().split()))
fast = min(a)

for i in range(len(a)):
	if a[i]==fast:
		ansI=i
		break
		
print(ansI+1,int(1.2*60*60/fast))
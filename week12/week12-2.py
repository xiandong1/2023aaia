a = list(map(int,input().split()))

ans = 0
for i in range(1,a[0]+1):
	ans +=a[i]
	
print(ans)
	
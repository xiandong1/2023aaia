a  = list(map(int,input().split()))

N=len(a)

ans=0
for i in range(N):
	if a[i]>0:
		ans+=a[i]

print(ans,end='')
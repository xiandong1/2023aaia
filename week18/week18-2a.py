a = list(map(int,input().split()))
if a[0]<a[1] : ans=-1
if a[0]>a[1] : ans=1
if a[0]==a[1] : ans=0

print(ans)
a = [9,8,7,6,5,4,3,2,1,0]

N=len(a)

print(a)

for i in range(N): 
  for k in range(N-1):
    if a[k] > a[k+1]:
      a[k],a[k+1] = a[k+1],a[k]

print(a)
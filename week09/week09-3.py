a = [1,3,5,7,9,11,13,15,17]
N=len(a)
for i in range(N-1):
  if a[i+1] - a[i]==a[1] - a[0]:
    print("現在的i是", i , "a[i]是" ,a[i], "相減是" , a[i+1]-a[i] , "\n相同")
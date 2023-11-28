def gcd(a ,b):
  print(a , b)
  if a == 0 :return b
  if b == 0 :return a
  return gcd(b , a%b)

a = 150000000
b = 205600000

print(gcd(a,b))
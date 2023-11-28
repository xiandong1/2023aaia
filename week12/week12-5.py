#輾轉相除法

a = 10000000000
b = 25005000000

c = a%b
print(a,b,c)

while c!=0:
  a = b
  b = c
  c = a%b 
  print(a,b,c)

print(b)
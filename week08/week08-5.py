a= int(input())

b = a

ans = 0
while b > 0:
	ans=ans*10+b%10
	b = b//10

print(f'{a}+{ans}={a+ans}')
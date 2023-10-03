a = int(input())
if a >= 90 :
	ans = "A"
if 90 > a >= 80 :
	ans = "B"
if 80 > a >= 70 :
	ans = "C"
if 70 > a >= 60 :
	ans = "D"
if a < 60 :
	ans = "F"
	
print(ans , end='')
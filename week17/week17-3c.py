a= input()

if "0"<=a<="9":
	ans="D"
elif "A"<=a<="Z":
	ans="U"
elif "a"<=a<="z":
	ans="L"
else:
	ans="O"
	
print(ans,end="")
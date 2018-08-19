def factorial(i):
	if i>1 :
		return i*factorial(i-1)
	else :
		return 1	
	
i=int(input())	
print(factorial(i))	
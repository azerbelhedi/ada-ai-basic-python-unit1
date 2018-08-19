def divisible(i):
	return (i%7)==0

def nonMulti(i):
	return (i%5)!=0

res =""		
for i in range(2000,3000) :
	if divisible(i) and nonMulti(i):
		#print(i)
		res += str(i)+" "
	
print(res)	


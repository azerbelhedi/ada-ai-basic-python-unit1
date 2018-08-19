import math
i = input("enter your list : ")
i=i.split(',')

h=30
c=50
res=""
for d in i:
	d=int(d)
	res=res+str(int(math.sqrt(int((2*d*c)/h))))+","
	print(int(math.sqrt(int((2*d*c)/h))))

print(res)	
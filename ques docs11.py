num=list(input("enter a number: "))
i=0
a=" "
while i<len(num):
	b=int(num[i])**2
	a=a+str(b)
	i=i+1
print(int(a))
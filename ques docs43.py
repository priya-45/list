a=[28,23,67,87,56,45,23,98,5,4,9,1,3,6,]
i=0
while i<len(a):
	if i%4==0 and i!=0:
		a.insert(i,20)
	i+=1
print(a)
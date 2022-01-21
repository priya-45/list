str="Priya S 1 2 3"
i=0
count,count1,count2,count3=0,0,0,0
while i<len(str):
	if str[i]>="a" and str[i]<="z":
		count=count+1
	elif str[i]>="A" and str[i]<="Z":
		count1=count1+1
	elif str[i]>="1" and str[i]<="9":
		count2=count2+1
	elif str[i]==" ":
		count3=count3+1
	i=i+1
print("upper case:",count1)
print("lower case:",count)
print("digit:",count2)
print('spaces:',count3)
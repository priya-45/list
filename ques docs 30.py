n=[2,-7,5,-64,-14]
i=0
count=0
count1=0
while i<len(n):
	if n[i]<0:
		count=count+1
	else:
		count1=count1+1
	i+=1
print("negative numbere:",count)
print("positive number:",count1)

a=["Hello preeti" ,"How are you"]
i=0
count=0
space=0
while i<len(a):
	space=space+1
	j=0
	while j<=len(a[i]):
		if a[i]>=" ":
			count=count+1
			b=a[i]
			c=j
		j=j+1
	i=i+1
	print(b,c,space)
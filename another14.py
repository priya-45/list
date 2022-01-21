a="i am priya"
b=a.split()
i=0
m=[]
while i<len(b):
	if i%2==0 and i!=0:
		b.insert(i,"space1")
		print(b)
	i=i+1
a=["priya","shilpkar","neha","rani","pooja","soni"]
i=0
n=[]
while i<len(a):
	j=1
	while j<len(a):
		c=a[i]+a[j]
		n.append(c)
		j=j+2
		i=i+2
print(n)
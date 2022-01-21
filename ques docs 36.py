a=['1','2','3', '4','5',' 6', '7','8']
i=0
n=[]
while i<len(a)-1:
	j=1
	while j<len(a):
		c=a[i]+a[j]
		n.append(c)
		j=j+2
		i=i+2
print(n)


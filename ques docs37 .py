a=[1,2,3, 4,5,6,]
i=0
n=[]
c=0
while i<len(a)-1:
	j=1
	while j<len(a):
		c=[a[i],a[j]]
		n.append(c)
		j=j+1
		i=i+1
print(n)
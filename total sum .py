number=30
n=[10,11,12,13,14,17,18,19]
i=0
l=[]
while i<len(n):
	j=i
	l2=[ ]
	while j<len(n):
		c=n[i]+n[j]
		if c==30:
			l2.append(n[i])
			l2.append(n[j])
			l.append(l2)
		j+=1
	i+=1
print(l)
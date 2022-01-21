num=[16,2,18,5,12,3]
i=0
n=[]
m=[]
while i<len(num):
	k=1
	c=0
	while k<=num[i]:
		if num[i]%k==0:
			c=c+1
		k=k+1
		b=num[i]
	if c==2:
		n.append(b)
	else:
		m.append(b)
	i=i+1
print(n,"prime") 
print(m,"not prime")
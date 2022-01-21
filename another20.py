num=int(input("enter number"))
i=1
n=[] 
count=0
while i<=num:
	j=1
	k=[]
	p=0
	while p<1:
		count=count+1
		n.append(count)
		p=p+1
	while j<=10:
			b=i*j
			k.append(b)
			j=j+1
	i=i+1
	n.append(k)
print(n)
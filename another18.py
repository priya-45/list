n=int(input("how many number you want:"))
a=[]
b=[]
c=[]
i=1
while i<=n:
	m=int(input("Enter number:"))
	a.append(m)
	if m%2==0:
		b.append(m)
	else:
		c.append(m)
	i=i+1
print(a)
print(b)
print(c)
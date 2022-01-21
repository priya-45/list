a=[12, 67, 98, 34]
i=0
n=[]
while i<len(a):
	c=a[i]%10
	d=a[i]//10
	sum=c+d
	n.append(sum)
	i=i+1
print(n)
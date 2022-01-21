a=[[1, 2, 4,], [2, 4, 4], [1,2]]
i=0
n=[]
while i<len(a):
	j=0
	sum=0
	while j<len(a[i]):
		sum=sum+a[j][i]
		j=j+1
	i=i+1
	n.append(sum)
print(n)

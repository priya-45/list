a=[[1, 2, 4,], [2, 4, 4], [1,2]]
i=0
n=[]
while i<len(a):
	j=0
	k=[]
	while j<len(a[i]):
		sum=a[j][i]
		k.append(sum)
		j=j+1
	i=i+1
	n.append(k)
print(n)
#o/p [[1, 2, 1], [2, 4, 2], [4, 4]]
a=[[5,6],8,5,[4,7]]
i=0
n=[]
while i<len(a):
	if type(a[i])==type([]):
		j=0
		while j<len(a[i]):
			n.append(a[i][j])
			j+=1
	i=i+1
print(n)
a=[[1,2,3,],[4,5,6,],[7]]
i=0
n=[]
m=[]
while i<len(a):
	j=0
	while j<len(a[i]):
		if a[i][j]%2==0:
			n.append(a[i][j])
		else:
			m.append(a[i][j])
		j=j+1
	i=i+1
print("even",n)
print("odd",m)
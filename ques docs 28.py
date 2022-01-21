a=[1, 1, 2, 3, 4, 5, 1, 2]
i=0
n=[]
while i<len(a):
	if a[i]!=1:
		n.append(a[i])
	i=i+1
print(n)
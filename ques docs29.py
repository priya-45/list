a=[5, 6, [], 3, [], [], 9]
i=0
n=[]
while i<len(a):
	if a[i]!=[]:
		n.append(a[i])
	i=i+1
print(n)

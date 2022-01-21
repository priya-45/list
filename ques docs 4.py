a=[3,1,3,5,6,3,1]
i=0
m=[ ]
while i<len(a):
	if a[i] not in m:
		m.append(a[i])
	i=i+1
j=0
n=1
while j<len(m):
	n=n*m[j]
	j+=1
print(n)
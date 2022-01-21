a=[6,2,3,5,4]
i=0
m=a[i]
while i<len(a):	
	if a[i]<m:
		m=a[i]
	i=i+1
print("minimum number=",m)
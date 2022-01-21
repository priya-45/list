a=[10,15,21,90,7,60]
i=0
n=[]
while i<len(a):
	if a[i]%10==0:
		n.append(a[i])
	i=i+1
print(n)

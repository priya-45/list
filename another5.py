a=['A','N','S','P','R','N','1','2','5','100',]
i=0
n=[]
m=[]
k=[]
while i<len(a):
	if a[i]>='A' and a[i]<='Z':
		n.append(a[i])
	if a[i]>='1' and a[i]<='9':
		m.append(a[i])
	i=i+1
j=0
while j<len(n):
	if a[j] not in k:
		k.append(a[j])
	j=j+1
print([k,m])
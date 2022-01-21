a=[1,2,3,4]
i=0
n=[]
n1=[]
while i<len(a):
	if a[i]%2==0:
		n.append(a[i])
	else:
		n1.append(a[i])
	i=i+1
print(n,"even")
print(n1,"odd")


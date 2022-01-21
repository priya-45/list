a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
i=0
n=[ ]
while i<len(a):
	while i<len(b):
		while i<len(c):
			k=a[i]+b[i]+c[i]
			n.append(k)
			i=i+1
print(n)
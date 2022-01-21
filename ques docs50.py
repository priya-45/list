a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
n=[ ]
while i<len(a):
	while i<len(b):
		k=a[i]+b[i]
		n.append(k)
		i=i+1
print(n)
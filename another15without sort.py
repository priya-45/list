a=[2,5,1,3,7,4]
i=0
n=[]
max=0
while i<len(a):
	if a[i]>max:
		max=a[i]
	i=i+1
j=1
while j<=max:
	if j in a:
		n.append(j)
	j=j+1
print(n)
# [1, 2, 3, 4, 5, 7]
# Without sort
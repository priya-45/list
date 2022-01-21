a=[[2,8,9],[9,8,9]]
i=0
sum=0
m=[]
while i<len(a):
	j=0
	sum1=0
	while j<len(a[i]):
		sum1=sum1+a[i][j]
		sum=sum1+1
		j=j+1
	m.append(sum1)
	i=i+1
j=0
n=1
while j<len(m):
	n=n*m[j]
	j=j+1
if n%2==0:
	print("even:",n)
else:
	print("odd:",n)	


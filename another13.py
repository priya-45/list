a=[32,32,42,87,99,42,44]
i=0
m=[]
n=[]
while i<len(a):
	if a[i] not in m:
		m.append(a[i])
	else:
		n.append(a[i])
	i=i+1
j=0
sum=0
while j<len(n):
	sum=sum+n[j]
	j=j+1
if sum%2==0:
	print("even sucessfull",sum)
else:
	print("odd not sucessfull",sum)
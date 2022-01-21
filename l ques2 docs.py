a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
sum=0
while i<len(a):
	j=0
	while j<len(a[i]):
		print(a[i][j],end="")
		j=j+1
	i=i+1
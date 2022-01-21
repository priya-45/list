char=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
a=[]
while i<len(char):
	count=0
	b=[]
	j=0
	while j<len(char):
		if char[i]==char[j]:
			count+=1
		j=j+1
	b.append(char[i])
	b.append(count)
	if b not in a:
		a.append(b)
	i+=1
print(a)
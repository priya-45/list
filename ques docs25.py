list=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
k=3
i=0
c=[]
while i<len(list):
	j=i
	count=0
	while j<len(list):
		if list[i]==list[j]:
			count+=1
			if count>=3:
				if list[i] not in c:
					c.append(list[i])
		j+=1
	i+=1
print(c)
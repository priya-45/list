list=[1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
while i<len(list):
	j=i
	count=0
	while j<len(list):
		if list[i]==list[j]:
			count+=1
			if count>=3:
				print(list[i])	
		j+=1
	i+=1
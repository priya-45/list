elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
while i<len(elements):
	if elements[i]%2==0:
		print("even",elements[i])
	else:
		print("odd",elements[i])
	i=i+1
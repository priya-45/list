numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7,26]
i=0
count=0
while numbers[i:]:
		number=numbers[i]
		if number>20 and number<40:
				count=count+1
		i=i+1
print(count)
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
count=0
count1=0
while i<len(elements):
	if elements[i]%2==0:
		sum=sum+elements[i]
		count=count+1
	else:
		sum1=sum1+elements[i]
		count1=count1+1
	i=i+1
even_avr=sum//count
odd_avr=sum1//count1
print("even average:",even_avr)
print("odd average:", odd_avr)
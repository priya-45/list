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
print("even count:",count)
print("odd count:",count1)
print("sum even:",sum)
print("sum odd:",sum1)
print("even average:",even_avr)
print("odd average:", odd_avr)
print("element in list count:",i)
sum2=sum+sum1
print("element ka sum :",sum2)
elem_avr=sum2//i
print("element ka average:",elem_avr)
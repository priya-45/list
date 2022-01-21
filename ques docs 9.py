number=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(number):
	if number[i]>max:
		max=number[i]
	i=i+1
j=0
nmax=0
while j<len(number):
	if number[j]>nmax:
		if number[j]<max:
			nmax=number[j]
	j=j+1
k=0
kmax=0
while k<len(number):
	if number[k]>kmax:
		if number[k]<nmax:
			kmax=number[k]
	k=k+1
print("first max number is:",max)
print("second max number is:",nmax)
print("third max number is:",kmax)
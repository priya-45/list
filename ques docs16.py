list=[1,2,3,4,5,6,7,8,9,10]
list.reverse()
i=0
a=1
n=[]
while i<len(list) and a<len(list):
	n.append(list[i]-list[a])
	a=a+1
	i=i+1
print(n)
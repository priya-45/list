a=["my name is gudia","i have apple"]
i=0
m=[]
while i<len(a):
	b=a[i].split()
	i=i+1
	m.append(b)
c=0
j=0
while j<len(m):
    k=0
    while k<len(m[j]):
        c=c+1
        print(m[j][k],c)
        k=k+1
    j=j+1

# j=0
# while j<len(m):
# 	 k=0
# 	 while k<len(m[j]):
	 	# c=c+1
	 	# print(m[j][k],c)
	#  	k=k+1
	#  j=j+1






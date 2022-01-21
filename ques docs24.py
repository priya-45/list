p= [1,2,3,1,2,2]
m=[ ]
i=0
while i<len(p):
	if p[i] not in m:
		m.append (p[i])
	i=i+1
print(m)

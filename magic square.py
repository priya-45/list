x= [
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]
]
i=0
a1,a2,a3,b1,b2,b3,c1,c2=0,0,0,0,0,0,0,0
while i<len(x):
	a1=a1+x[0][i]
	a2=a2+x[1][i]
	a3=a3+x[2][i]
	b1=b1+x[i][0]
	b2=b2+x[i][1]
	b3=b3+x[i][2]
	c1=c1+x[i][i]
	c2=c2+x[i][2-i]
	i=i+1
if a1==a2==a3==b1==b2==b3==c1==c2:		
    print("magic square")
else:
	print("not magic square")
a=["geetu sharma","from sarjapur"]
i=0
while i<len(a):
    b=a[i].split()
    i=i+1
    j=0
    while j<len(b):
        k=0
        count=0
        while k<len(b[j]):
            count=count+1
            v=b[j]
            c=k
            k=k+1
        j=j+1
        print(v,j,count)

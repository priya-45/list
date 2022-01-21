list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
n=[]
while i<len(list1):
    if i not in list2:
        n.append(i)
    i=i+1
print(n)
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]]
i=0
sum=0
while i<len(marks):
    j=0
    sum1=0
    while j<len(marks[i]):
        sum1=sum1+marks[i][j]
        j=j+1
        sum1=sum+sum1
    avr=sum1//len(marks[i])
    print("average of",1+i,"year",avr)
    i=i+1
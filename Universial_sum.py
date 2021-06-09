num=[1,2,3,[4,5],6,7,[8,9],1,2,3,[4,5]]
i=0
sum=0
while i<len(num):
    if type(num[i])==type(num):
        j=0
        while j<len(num[i]):
            sum=sum+num[i][j]
            j=j+1
    else:
        sum=sum+num[i]
    i=i+1
print(sum)        
num=[0,0,0,1,1,1,2,2,3,3,4,4,4]
j=0
for i in range(len(num)):
    if (num[i]!=num[i-1]):
        num[j]=num[i]
        j+=1
print(num)
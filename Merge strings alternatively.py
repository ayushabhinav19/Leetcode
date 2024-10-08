word1="abc"
word2="pqr"

# form an empty list
merged=[]

# finding the maximum length to run the loop
length=max(len(word1),len(word2))

for i in range(0,length):
    if i < len(word1):
        merged.append(word1[i])
    if i < len(word2):
        merged.append(word2[i])

#making list as string
join="".join(merged)
print(join)

#output= "apbqcr"
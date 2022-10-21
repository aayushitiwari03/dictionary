dic={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['ZacharySimon']}
dict1={}
for x in dic:
    lis=dic[x]
    i=0
    while i<len(lis):
        dict1[x]=lis[i]
        i+=1
print(dict1)

lis=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
'Zachary Simon', 'VII']]
dic={}
i=0
while i<len(lis):
    j=0
    while j<len(lis[i]):
        if type(lis[i][j])==int:
            x=lis[i][j]
            del lis[i][j]
        else:
            dic[x]=lis[i]
        j+=1
    i+=1
print(dic)


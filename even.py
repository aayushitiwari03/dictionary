dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
for x in dic:
    if type(dic[x])==list:
        lis=dic[x]
        even=[]
        i=0
        while i<len(lis):
            if lis[i]%2==0:
                even.append(lis[i])
            i+=1
        dic.update({x:even})
print(dic)
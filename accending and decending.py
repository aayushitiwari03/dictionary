dic={'aayushi':7,'roopa':5,'shaina':6,'kajal':5,'kamini':6}
for i in dic:
    for j in dic:
        if dic[i]>dic[j]:
            dic[i],dic[j]=dic[j],dic[i]
print(dic)
dic=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
dic1=[]
for x in dic:
    for y in x:
        if x[y] not in dic1:
            dic1.append(x[y])
print(dic1)
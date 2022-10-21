dic={"aayushi":7,"dali":4,"roshni":6,"roopa":4,"shaina":6}
max=0
min=dic['aayushi']
for i in dic:
    if dic[i]>max:
        max=dic[i]
    elif dic[i]<min:
        min=dic[i]
print("maximum is = ",max,"\n","minimum is =",min)
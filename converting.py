lis=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
dic={}
e=[]
o=[]
st=[]
for x in lis:
    for y in x:
        if type(y)==str:
            if y not in st:
                st.append(y)
        else:
            if y%2==0:
                e.append(y)
            else:
                if y not in o:         
                    o.append(y)
i=0
while i<len(st):
    if i%2!=0:
        dic.update({st[i]:e})
    else:
        dic.update({st[i]:o})
    i+=1
print(dic)
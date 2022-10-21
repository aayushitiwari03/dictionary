dic={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
dict1={}
for x in dic:
    if dic[x]>170:
        dict1.update({x:dic[x]})
print(dict1)
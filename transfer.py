dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dic1={}
# c=0
# for x,y in dic.items():
#     for y in dic.values():     
#         dic1[y]=len(y)
# print(dic1)
        

# red': 3, 'green': 5, 'black': 5, 'white': 5}

for x in dic.values():
    dic1[x]=len(x)
print(dic1)


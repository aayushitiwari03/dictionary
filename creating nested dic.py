# ................WITH WHILE LOOP..................

# l=int(input("enter : "))
# dic={}
# i=0
# while i<l:
#     key=input("enter  the key: ")
#     vl=int(input("enter the lenght for value : "))
#     j=0
#     b=[]
#     while j<vl:
#         value=input("enter the value for key : ")
#         b.append(int(value))
#         j+=1
#     dic.update({key:b})   
#     i+=1
# print(dic)


# ...................WITH FOR LOOP......................


l=int(input("enter : "))
dic={}
for i in range(l):
    key=input("enter  the key: ")
    vl=int(input("enter the lenght for value : "))
    b=[]
    for j in range(vl):
        value=input("enter the value for key : ")
        b.append(int(value))
    dic.update({key:b})   
print(dic)



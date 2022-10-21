def it(dic):
    c=0
    for x in dic:
        c+=1
        print(x,"\t",dic[x],"\t",c)
print("keys","\t","value","\t","count")
it({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})

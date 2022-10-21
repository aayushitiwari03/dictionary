d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for x in d1:
    if x in d2:
        d2[x]=d1[x]+d2[x]
    else:
        d2[x]=d1[x]
print(d2)


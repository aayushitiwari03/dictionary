a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
cp={}
for d in a:
    if d['item'] not in cp:
        cp[d['item']] = d['amount']
    else:
        cp[d['item']] += d['amount'] 
print(cp)




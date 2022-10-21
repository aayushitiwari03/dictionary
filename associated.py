student = [{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False,
 'name': 'Rabi'},
{'id': 3, 'success': True, 
'name': 'Alex'}]
sum=0
key=input("enter key : ")
for x in student:
    for y in x:
        if y==key:
                sum=sum+x[y]
print(sum)



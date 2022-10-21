#   example............

# dict1= {"brand":"suzuki","model":"dzire","year":2020}
# print(dict1)

# accessing items.........................

# dict1= {"brand":"suzuki","model":"dzire","year":2020}
# print(dict1)
# x=dict1["model"]
# print(x)

# loop through a dictionary...................

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# for x in dict1:
#     print(x)

# "this will print the index value (means key)"..

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# for x in dict1:
#     print(dict1[x])

#  this will print the value..

#  ............................. METHODS...................................

#  we can use the value() the function to return values of dictionary:........

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# for x in dict1.values():
#     print(x)


#  we can also use the items () functions to return values of dictionary:..........

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# for x,y in dict1.items():
#     print(x,y)


# len = this function is used to find length of the dictionary.......

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# x=len(dict1)
# print("dictionary lenght is = ",x)

# pop() = this method removes the element with the specified key name .....

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# dict1.pop('brand')
# print(dict1)

# popitem() = this method removes the last elements of the dictionary but in the 
# version berfore 3.7 it was used to remove the random value 

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# dict1.popitem()
# print(dict1)


# del = this keyword removes the item with specified key name  and it can also delet 
# the whole dictionary.....

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# del dict1['brand']
# print(dict1)


# clear = clear the dictionary and gives the empty dictionary.....

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# dict1.clear()
# print(dict1)

# copy = it will print the values in the dictionary along with keys

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# x=dict1.copy()
# print(x)

# fromkeys = the fromkeys method returns a dictionary with the specified keys and 
# the specified value.

# x=('firstkey','secondkey','thirdkey')
# y=0
# dict1=dict.fromkeys(x,y)
# print(dict1)


# setdefault = the stedfault method returns the values of the item with the specified
# key and if thet key does not exist it inserts the key , with specified value

# dict1={'brand':'suzuki','model':'dzire','year':2020}
# dict1.setdefault('color','black')
# print(dict1)

# update =  The update method inserts the specified items to dictionary.

# dict1={"brand":"suzuki","model":"dzire","year":2020}
# dict1.update({"color":"erty"})
# print(dict1)
# ....................RECURSION.................
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return (n+sum(n-1))
# n=int(input("enter the number : "))
# x=sum(n)
# print(x)

# def fac(n):
#     if n==0:
#         return 1
#     else:
#         return (n*fac(n-1))
# n=int(input("enter the number : "))
# x=fac(n)
# print(x)



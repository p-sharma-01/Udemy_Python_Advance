new_list=[a+1 for a in [1,2,3] ]
print(new_list)
new_l=[a**2 for a in range(1,5)]
print(new_l)

# conditional list comprehension
s=[a for a in range(1,10) if a%2==0 ]
print(s)

#name having length 3   
names=['raj','kanha','ppsh','ram','shyam']
sa=[a for a in names if len(a)==3]
print(sa)

# list c practice
d=[1,2,3,4,8,21,34,55]
even=[a for a in d if a%2==0]
square=[a**2 for a in d ]
print(even,square,sep="\n")
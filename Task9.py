dictionary={ 'Alice':'85', 'Ben':'68', 'Smith':'92', 'Adam':'78','Joe':'45'}
a=input("Enter the student's name:" )
if a in dictionary:
    print(a,"'s marks:",dictionary[a])
else:
    print('Student not found')
#Declaring tuple data types
#Tuple is immutable it can also access any values

tup1 =  4,9,8,10,12,15,22,7,2
tup2 = 'Elsa',"Anna",2000,"spiderman","super hero",1000
tup3 =  ()
tup4 =  (10,)
tup5 = "Rockhill",4564,"l5z 2th"


print(tup1,type(tup1),len(tup1),id(tup1))
print(' ')
print(tup2,type(tup2),len(tup2),id(tup2))
print(' ')
print(tup3,type(tup3),len(tup3),id(tup3))
print(' ')
print(tup4,type(tup4),len(tup4),id(tup4))
print(' ')
print(tup5,type(tup5),len(tup5),id(tup5))


print(tup1[3])
print(tup2[-2])
print(tup1[:3])
print(tup2[:4])
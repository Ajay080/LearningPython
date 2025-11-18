import copy
a=[23, 432,432,[23, 32,42], 32]
b=a.copy() #shallow copy
print("Original list a:", a)
print("Shallow copied list b:", b)
b[3][0]=999
print("After modifying b[3][0] to 999")
print("List a:", a)  # a is also affected
print("List b:", b) # b is affected


d=list(a)
print("Copied list d using list():", d)
a[3][1]=555
print("After modifying a[3][1] to 555")
print("List a:", a)  # a is affected
print("List d:", d) # d is also affected
a[0]=111
print("After modifying a[0] to 111")
print("List a:", a)  # a is affected
print("List d:", d) # d is not affected

c= copy.deepcopy(a) #deep copy
print("Deep copied list c:", c)
c[3][1]=888
print("After modifying c[3][1] to 888")
print("List a:", a)  # a is not affected
print("List c:", c) # c is affected

print(1==3)  #False
print(1!=3)  #True
print(1>3)   #False
print(1<3)   #True
print(1>=3)  #False
print(1<=3)  #True
print(1<3-1)  #False # first 3-1 is evaluated then 1<2
print(1<3 and 2<3)  #True
print(1<3 or 2>3)  #True
print(not(1<3))  #False
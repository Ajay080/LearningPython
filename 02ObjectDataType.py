#Number
a=int('121')
print("type of a is", type(a), "and value is", a)

#Float
b=float("12.34")
print("type of b is", type(b), "and value is", b)

# String
c=str(123.45)
print("type of c is", type(c), "and value is", c)
# c[0]='A'  #Strings are immutable will gives you error

#List
d=list([1,2,3,4,5])
print("type of d is", type(d), "and value is", d)
d[0]=[10,20,30]
print("After modification, value of d is", d)
d.extend([6,7,8])
print("After extending, value of d is", d)
d.append(9)
print("After appending, value of d is", d)
d.remove(3)
print("After removing 3, value of d is", d)
d.pop()
print("After popping last element, value of d is", d)
d.clear()
print("After clearing, value of d is", d)
d.count(2)
print("Count of 2 in d is", d.count(2))
print("After inserting 10 at index 0, value of e) is", d)
d.insert(0,10)
print("After inserting 10 at index 0, value of d is", d)
d.sort()
print("After sorting, value of d is", d)
d.reverse()
print("After reversing, value of d is", d)
d.reverse()
print("After reversing, value of d is", d)
print("Index of 10 in d is", d.index(10))
print("is 5 present in d?", 5 in d)

#sort a 2d list based on second element
d2= [[1,3], [4,1], [5,2]]
d2.sort(key=lambda x: x[1])
print("After sorting based on second element, value of d2 is", d2)

#sort a 2d list based on first element
d2.sort(key=lambda x: x[0])
print("After sorting based on first element, value of d2 is", d2)

#sort a list of strings based on length
d3= ["apple", "banana", "kiwi", "cherry", "blueberry"]
d3.sort(key=lambda x: len(x))
print("After sorting based on length, value of d3 is", d3)

#sort a list of strings based on alphabetical order
d3.sort()
print("After sorting based on alphabetical order, value of d3 is", d3)

#sort a list of strings based on reverse alphabetical order
d3.sort(reverse=True) #same as key=lambda x: x[::-1] and d.reverse()
print("After sorting based on reverse alphabetical order, value of d3 is", d3)

#sort on the basis of first and last value
d4= ["apple", "banana", "kiwi", "cherry", "blueberry"]
d4.sort(key=lambda x: (x[0], x[-1]))
print("After sorting based on first and last character, value of d4 is", d4)

d4.sort(key=lambda x: (x[-1], x[0]))
print("After sorting based on last and first character, value of d4 is", d4)

del d
# print("After deleting, value of d is", d)  #Will give error as d

#Tuple
e=tuple((1,2,3,4,5))
print("type of e is", type(e), "and value is", e)
# e[0]=10  #Tuples are immutable will gives you error   
# e.clear() #Tuples do not have clear method will gives you error
print("After clearing, value of e is", e)
del e
# print("After deleting, value of e is", e)  #Will give error as e is deleted


#Dictionary
f=dict({"name":"John", "age":"30", "city":"New York"})
print("type of f is", type(f), "and value is", f)
f["age"]="31"
print("After modification, value of f is", f)
f["country"]="USA"
print("After adding country, value of f is", f)
del f["city"]
print("After deleting city, value of f is", f)
print("accessing name from f gives", f["name"])
print("accessing city from f gives", f.get("city", "Not Found"))
#accessing keys only
print("Keys in dictionary is", f.keys())
#accessing values only
print("Values in dictionary is", f.values())
#accessing key-value pairs
print("Key-Value pairs in dictionary is", f.items())

#sort a dictionary based on keys
sorted_keys= sorted(f.keys())
print("Sorted keys are", sorted_keys)
#sort a dictionary based on values
sorted_values= sorted(f.values())
print("Sorted values are", sorted_values)

for key,value in f.items():
    print("Key is", key, "and Value is", value)
    pass

#sort by alphabetic
f=dict(sorted(f.items(), key=lambda x: x[0]))
print("After sorting based on keys, value of f is", f)
#sort by values
f= dict(sorted(f.items(), key=lambda x: x[1]))
print("After sorting based on values, value of f is", f)    
# set
g= set([1, 2, 3, 4, 5])
print("type of g is", type(g), "and value is", g)
g.add(6)
print("After adding 6, value of g is", g)
print("Is 3 present in g?", 3 in g)
g.remove(3)
print("After removing 3, value of g is", g)
g.discard(10)  # No error if element not found
print("After discarding 10, value of g is", g)
g.pop()
print("After popping an element, value of g is", g)
#how to iterate through set
for item in g:
    print("Item in set g is", item)
    break
g.clear()
print("After clearing, value of g is", g)
del g
# print("After deleting, value of g is", g)  #Will give error as g is deleted


#boolena
a=True
print("type of a is", type(a), "and value is", a)
a=bool(1)
print("type of a is", type(a), "and value is", a)
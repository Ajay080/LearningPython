chai="Hi may I help you ? "

chai = chai.strip()
print("After stripping, value of chai is:", chai)

chai = chai.upper()
print("After converting to upper case, value of chai is:", chai)

chai = chai.replace("?", "!!!")
print("After replacing ?, value of chai is:", chai) 

chai = chai.split(" ")
print("After splitting, value of chai is:", chai)

chai = " ".join(chai)
print("After joining, value of chai is:", chai)

chai= "   Hi may I help you ?   "
print(chai.find("help"))  #prints index of first occurrence of help
print(chai.find("hello"))  #prints -1 as hello is not present
print(chai.startswith("Hi"))  #True
print(chai.endswith("?"))  #True

print(chai.count(" "))  #prints number of spaces in the string

#String Formatting
name= "Ajay"
age= 25
intro= "My name is {} and I am {} years old.".format(name, age)
print(intro)

chai= "My name is {0} and I am {1} years old. {0} is learning Python.".format(name, age)
print(chai)

intro= f"My name is {name} and I am {age} years old."
print(intro)


chai= "Hew ,\n \"Sdsa\" sdas"
print(chai)

chai= r"Hew ,\n \"Sdsa\" sdas"
print(chai)

print ("Hello" in chai)  #False
print ("Hew" in chai)    #True
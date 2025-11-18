import math 
import random
print(math.pi)  #3.141592653589793
print(math.floor(3.7))  #3
print(math.floor(-3.7))  #-4
print(math.ceil(3.3))   #4
print(math.sqrt(16))    #4.0
print(math.pow(2, 3))   #8.0
print(math.factorial(5)) #120
print(math.gcd(48, 18))  #6
print(math.lcm(4, 6))    #12
print(math.sin(math.pi/2))  #1.0
print(math.cos(0))         #1.0
print(math.tan(math.pi/4)) #1.0
print(math.log(100, 10))   #2.0
print(math.exp(2))         #7.38905609893065

#trunc is different from floor, it removes the decimal part without rounding towards 0
print(math.trunc(3.7))  #3.0
print(math.isclose(0.1 + 0.2, 0.3))  #True
print(math.isnan(float('nan')))  #True
print(math.isinf(float('inf')))  #True
print(math.degrees(math.pi/2))  #90.0

print(random.random())  #random float between 0.0 to 1.0
print(random.randint(1, 10))  #random integer between 1 to 10
print(random.choice(['apple', 'banana', 'cherry']))  #random choice from the list
print(random.sample(range(1, 100), 5))  #random sample of 5 unique numbers from 1 to 99
print(random.uniform(1.0, 10.0))  #random float between 1.0 to 10.0

random.random()
randome.choice(['apple', 'banana', 'cherry'], k=2)  #Error, k is not valid for choice
randdome.randint(1,100)
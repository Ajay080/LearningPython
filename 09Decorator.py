#decorators: “Tools that wrap another function to add extra features.”

#timing function execution

import time


def timeDecoraor(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        result=func(*args, **kwargs)
        end_time=time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timeDecoraor
def sample_function(n):
    total=0
    for i in range(n):
        total+=i
    return total

res=sample_function(1000000)
print("Result of sample_function:", res)


#debug function call

def debugDecorator(func):
    def wrapper(*args, **kwargs):
        print(f"CCalling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result=func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@debugDecorator
def add(a, b):
    return a + b

sum_result=add(5, 10)
print("Sum result:", sum_result)
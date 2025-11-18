x = 10

def func4():
    global x
    x += 5
    print("Inside func4:", x)

func4()
print("Inside func3:", x)
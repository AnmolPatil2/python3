def simpleGeneratorFun():
    print("Gener")
    yield 1
    yield 2
    return 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
    print("s")

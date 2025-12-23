def my_generator():
    yield 1
    print("this is a generator")
    yield 2
    yield 3
    yield 4
    return 5

for i in my_generator():
    print(i)
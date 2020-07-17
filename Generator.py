def gen123():
    print("First round")
    yield 1
    print("Second round")
    yield 2
    print("Third round")
    yield 3

it = gen123()
print(next(it))
print(next(it))
print(next(it))
print(next(it))

def gen123():
    print("First round")
    yield 1
    print("Second round")
    yield 2
    print("Third round")
    yield 3

it = gen123()
it = (i for i in range(1,4)) # Short syntax

print(next(it))
print(next(it))
print(next(it))
print(next(it))

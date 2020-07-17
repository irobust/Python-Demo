def sequence():
    yield 1,1
    yield 2,1
    yield 3,2
    
    count=4
    a = 1
    b = 2
    while True:
        yield count, a+b
        count += 1
        # a = b
        # b = a + b
        a, b = b, a+b
        if b > 100: break       # Remove this line when you need infinite loop

for k,v in sequence():
    print(f"{k} => {v}")

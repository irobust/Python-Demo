def basic(a: int, b: int, c: int = 20) -> int:
    return a + b + c

ans = basic('a', 'b', 'c')
ans = basic(1, 2, 3)


def multipleArguments(firstArgs=0, *args):
    sum = 0
    for item in args:
        sum += item
    return args

multipleArguments(1,2,3,4)

def keyValueArguments(firstArgs, **args):
    print(args['firstname'] + ' ' + args['lastname'] + '' + args['age'])

keyValueArguments(0, lastname='Doe', firstname='John')

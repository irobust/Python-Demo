def minmax(*args):
    if(len(args)):
        for number in args:
            print(number)
    return min(list(args)), max(list(args)), sum(list(args))/len(list(args))

def doSomething(**args):
    if(len(args)):
        for key in args:
            print(key, args[key])

doSomething(k1="text1", k2="text2")

min, _, avg = minmax(1,2,3,4,5,6,7,8)
pass
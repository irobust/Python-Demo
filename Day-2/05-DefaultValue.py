import time

def show_default(arg=time.ctime()):
    print(arg)

def add_spam(arg=None):
    if arg is None: arg= []
    arg.append('spam')
    print(arg)

add_spam()
add_spam()
add_spam()

show_default()
time.sleep(5)
show_default()
time.sleep(5)
show_default()
class Animal:
    def __init__(self, **args):
        self._type = args['type'] if 'type' in args else 'cat'

    def gettype(self):
        return self._type

class Duck(Animal):
    def __init__(self, **args):
        if 'type' in args: del args['type']
        args['type'] = 'duck'
        super().__init__(**args)

def main():
    donald = Duck(type='Dog')
    print(f"I'm a {donald.gettype()}")

if __name__ == '__main__': main()


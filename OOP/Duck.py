class Duck:
    _sound = 'Quack Quack'
    _movement = 'Walk like a duck'
    _numbers = [1,2,3,4,5]
    _i = 0

    def __init__(self, **args):
        self._name = args['name'] if 'name' in args else 'donald'
        self._i = args['i'] if 'i' in args else 0

    def quack(self):
        print(self._sound)

    def move(self):
        print(self._movement)

    def __str__(self):
        return f"Hello, I'm {self._name}"

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= len(self._numbers):
            raise StopIteration
        self._i += 1
        return self._numbers[self._i]

def main():
    donald = Duck()
    print(donald._sound)
    donald.move()

    print(donald)

if __name__ == '__main__': main()



def inclusive_range(start=0, stop=1, step=1):
    try:
        i = int(start)
    except (TypeError, ValueError) as e:
        raise TypeError(f'Invalid start, You must input number {e!r}')
        return 

    if(start <= 0): raise ValueError('Start must higher than 0')

    while(i <= stop):
        yield i
        i += step

def main():
    for i in inclusive_range(-1, 10):
        print(i)

    # i = iter(inclusive_range(1, 10))
    # pass


if(__name__ == '__main__'): main()
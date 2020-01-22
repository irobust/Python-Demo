import os

print(os.name)
print(str(os.path.exists('test.txt')))
print(str(os.path.isfile('test.txt')))
print(str(os.path.isdir('test.txt')))

print(str(os.path.realpath('test.txt')))
print(str(os.path.split(os.path.realpath('test.txt'))))

directory, filename = os.path.split(os.path.realpath('test.txt')

# from os import path

# f = open("test.txt", "a")

# for i in range(10):
#     f.write(f'This is a test message {i+1}\n')

# f = open("test.txt", "r")
# if f.mode == 'r':
#      lines = f.readlines()

#      for line in lines:
#          print(line)


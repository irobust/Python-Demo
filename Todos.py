from urllib.request import urlopen
import json
import pprint

def main():
    targetURL = "https://jsonplaceholder.typicode.com/todos"
    response = urlopen(targetURL)

    if (response.getcode() == 200):
        data = response.read()

        todos = json.loads(data)
        for i in range(5):
            for key in todos[i]:
                print(key, todos[i][key])
            print('\n-----------\n')
    else:
        print("Some error happen, Can't retrive results")

if(__name__ == '__main__'):
    main()
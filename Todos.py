def output(todos):
    import pprint as pp

    pp.pprint(todos)
    print(todos[0]['title'])

def handleResponse(response):
    import json

    if response.getcode() == 200:
        data = response.read()
        todos = json.loads(data)
        output(todos)
    else:
        print("Some error happen, Can't get any results")
    

def getTodos():
    from urllib.request import urlopen
    
    targetURL = "https://jsonplaceholder.typicode.com/todos"
    response = urlopen(targetURL)
    handleResponse(response)

        
def main():
    getTodos()


if __name__ == '__main__':
    main()

import json

x = '{ "name":"John", "age":30, "city":"New York"}'
z = { "name":"John", "age":30, "city":"New York"}

y=json.loads(x) #convert from json to  python by json.loads()
print(y['age'])

y=json.dumps(z) # convert from python to json by json.dumps()
print(y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y=json.dumps(x, indent=4, separators=('. ', ' = '))
print(y)
y=json.dumps(x,indent=4, sort_keys=True)
print(y)
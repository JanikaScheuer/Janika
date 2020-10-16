name = 'Lorenz'
age = 21

print(f'The current month is {name}')

d = [
  {
  'name': 'lorenz',
  'age': 24
  },
  {
  'name': 'janika',
  'age': 99
  }
]

for person in d:
  name = person['name']
  age = person['age']
  print(f'This client is called {name} and is {age} years old')
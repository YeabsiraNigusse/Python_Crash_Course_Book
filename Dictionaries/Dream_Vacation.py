from genericpath import samefile


cities = {}
while True:
    name = input('what is your name ')
    response = input(' If you could visit one place in the world, where ' 
    'would you go? ')
    cities[name] = response
    permission = input('is there any one who can take our poll "yes/no" ')
    if permission.lower() == 'no':
        break
print()
for name, city in cities.items():
    print(f'if {name} get the chance to go, he would like to go {city}')
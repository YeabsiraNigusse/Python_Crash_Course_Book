Glossary = {}
Glossary['Dictionaries'] = 'a collection of key-value pairs'
Glossary['List'] = 'collection of items in particular order'
Glossary['Variable'] = 'labels associated with some value'
print()
# print('Dectionaries : ',Glossary.get('Dictionaries'))
# print('List : ',Glossary.get('List'))
# print('Variable : ', Glossary.get('List'))
for word,definition in Glossary.items():
    print(f"{word} is {definition}")
print()
for word in Glossary.keys():
    print(f'{word}')
print()
for definition in Glossary.values():
    print(f'{definition}')
print()
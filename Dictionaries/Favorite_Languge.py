Favorite_Languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'sami':'python',
    'yeab': 'c++'
}
# list = ['yeab','sami','tedi','jen','sarah']

# for name in Favorite_Languages.keys():
#     if name in list:
#         print(f'{name.title()} thank you for taking this poll')
#         print()
#     else:
#         print(f'{name.title()} please take our poll')
#         print()

s = '[]{}(()'
def parentesis(k):
    s = {'(':')','{':'}','[':']'}
    Stack = []
    for i in k:
        if i == s.keys():
            Stack.append(i)
            print(Stack)
        elif i ==s.values():
            if Stack:
               Stack.pop()
               print(Stack)
    return True if not Stack else False
print(parentesis(s))


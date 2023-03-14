path = 'Files/Learning_python.txt'
pythonString = ''
with open(path) as file:
    lines = file.readlines()
print(lines)

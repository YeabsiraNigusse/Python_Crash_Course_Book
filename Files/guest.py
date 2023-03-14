path = 'Files/guest.txt'
while True:
    name = input('what is your name')
    name+=' \n'
    with open(path,'a') as file:
       file.write(name)
       per = input('do you want to continu yes/no')
       if per.lower() == 'no':
        break
with open(path) as file:
   content =  file.read()
   print(content)

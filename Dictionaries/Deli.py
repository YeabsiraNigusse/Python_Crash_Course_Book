Food_Orders = ['doro', 'shiro','doro', 'Beyayinet', 'doro','atikilt','firfir']    
Finished_Foods = []
while Food_Orders:
    if 'doro' in Food_Orders:
        print("I am run out of doro ")
        while 'doro' in Food_Orders:
          Food_Orders.remove('doro')
    food = Food_Orders.pop()
    print(f' I made your {food} ')
    Finished_Foods.append(food)
print()
print(Finished_Foods)
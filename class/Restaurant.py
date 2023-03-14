class Restaurant:
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        describe = f'the name of the restaurant is {self.restaurant_name} and it is {self.cuisine_type} hotel'
        return describe
    def open_restaurant(self):
        print("it's open")
    def set_number_served(self,number):
        self.number_served = number
    def increment_number_served(self):
        self.number_served+=1

    
my_restaurant = Restaurant('misrak ber', 'five star')
print(my_restaurant.describe_restaurant())
Restaurant2 = Restaurant('Ozon','five star')
print()
my_restaurant.open_restaurant()
print(Restaurant2.number_served)
Restaurant2.set_number_served(10)
print(Restaurant2.number_served)
Restaurant2.increment_number_served()
print(Restaurant2.number_served)

class IcecreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
    def flavors(self,*flavors):
          for flavor in flavors:
            print(flavor.title())
print(Restaurant2.describe_restaurant())
icecream = IcecreamStand('chuchi','3 star')
print(icecream.describe_restaurant())
icecream.flavors('mango flavor', 'avocado flavor', 'banana flavor')
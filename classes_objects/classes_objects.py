#Example class
#A class is like a recipe that makes a cake
#A class is like a recipe
#The object is what you make with the recipe 
class Car:
    #The brand, model, color are the attributes of the Car class
    #Can be seen as ingredients for the recipe 
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        
    #Define a method (and action/behavior) the car can do
    #also are like directions for the car class
    def drive(self):
            return 'Vroom'
        
    def honk(self):
            return 'Beep Boop'
        
brand = input('Enter the brand name of your car: ')
model = input('Enter the model of your car: ')
color = input('Enter the color of your car: ')
        
        
my_car = Car(brand, model, color)

#Below are a bunch of objects create from the Car class
print(my_car.brand)
print(my_car.model)
print(my_car.color)
print(my_car.drive())
print(my_car.honk())
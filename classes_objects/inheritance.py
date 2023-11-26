#Base class
class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_vehicle_info(self):
        return (f'Make: {self.make}, Model: {self.model}')
    
    #Derived Class: A derived class is defined by passing in the base class (Vehicle) 
    #as a class parameter
class Car(Vehicle):
    def __init__(self, make, model, horsepower):
        #The super() function calls the __init__ method from the Vehicle class
        #This allows you to use the variables in the Vehicle class
        super().__init__(make, model)
        self.horsepower = horsepower
    
    def display_car_info(self):
        return (f'{super().display_vehicle_info}, Horsepower: {self.horsepower}')
            
            
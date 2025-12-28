# basic class and object


class Car:
    # barnd = None
    # model = None
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model

    def full_name(self ,  ):
        return f"{self.brand} {self.model}"

    




class ElectricCar(Car):
    def __init__(self, brand, model , battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size








# Inheritance  :  create  an ElectricCar class that inherits from the car class and has an additional 
                #   additinonal attribute battry size

my_tesla = ElectricCar("Tesla" , "Model S" , "300KWH")
print(my_tesla.full_name())
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)








# __init___ constctor methad hai
my_car = Car("Toyta" , "Corolla")
print(my_car.brand)   
print(my_car.model)   
print(my_car.full_name())





my_new_car = Car("tata" , "safari")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())

# class Method and Self
# add method to the car class that dispaly the full nam of the car






# /////////////////////////////////////

# Encapsulations - - capuse ke type
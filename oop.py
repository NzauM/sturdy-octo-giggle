class Student:
    def __init__(self, first_name_received, last_name_received, adm_no_received):
        print("Initializing Student Object")
        self.first_name = first_name_received
        self.last_name = last_name_received
        self.adm_no = adm_no_received

    def sampleFunc():
        pass
    pass

# isaac = Student("Isaac", "Kuria", 300) 
# isaac is an object created from class Student
# we created him by invoking/calling the class. And this in OOP is called instantiation
# isaac is now an instance of our Student Class
# javan = Student("Javan","Abbot",301)

# hope = Student("Hope","Makanda",302)

# user_name = "mercy"
# user_name.lower()


# print(type(isaac))

class Car:
    # how will cars be built, Attributes: model, yom, engine_capacity, horse_power, color
    def __init__(self, model_received, yom_received, engine_capacity_received, horse_power_received, color_received):
        self.model = model_received
        self.yom = yom_received
        self.engine_capacity = engine_capacity_received
        self.horse_power = horse_power_received
        self.color = color_received
        print(f"{self.model} has been created successfully")
        pass

    # define how that attribute will be accessed (getter method)
    # define how that attribute will be set/passed/added(setter method)
    # define a property variable and call the property function and passs the getter, setter

    def get_engine_capacity(self):
        resp = f"{self.model} has an engine capacity of {self._engine_capacity}" 
        return resp
        # return self.engine_capacity
    def set_engine_capacity(self,new_engine_capacity):
        if new_engine_capacity < 2000:
            print("This is an Invalid Car")
        else:
            self._engine_capacity = new_engine_capacity
            print("Engine Capacity Changed")
        pass

    engine_capacity = property(get_engine_capacity,set_engine_capacity)


    pass



rynes_car = Car("Camrey", 2023, 2000, "300", "Pink")
brendahs_car = Car("Lexus", 2020, 2200, "500", "Silver")

rynes_car_model = rynes_car.model
rynes_car_color = rynes_car.color
brendahs_car_horsepower = brendahs_car.horse_power
print(rynes_car.engine_capacity)
rynes_car.engine_capacity = 300
print(rynes_car.engine_capacity)



# Ryne Drives a Pink Camrey model 2023 with 2000cc and a 300 horsepower
# print(f"Ryne drives a {rynes_car.color} {rynes_car_model} model {rynes_car.engine_capacity} and a {rynes_car.horse_power} horsepower")

# Getters and Setters








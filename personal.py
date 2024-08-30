personDeets = {"name":"Mercy Nzau", "password":1234, "is_admin":False}

# def authenticateDecorator(decoratedlogin):
#     def check_is_admin():
#         if not personDeets['is_admin']:
#             return decoratedlogin()
#         else:
#             return ("Admin hawezi login")
#     return check_is_admin

# @authenticateDecorator
# def logIn():
#     if personDeets["name"] == "Mercy Nzau" and personDeets["password"] == 1234:
#         return "Logged in Succesfully"
#     else:
#         return "We si admin, na huna credentials, unadai?"
    
    
# print(logIn())
# def authenticate(func):
#     def authLogin():
#         if personDeets["is_admin"]:
#             return "An Admin does not need to login"
#     return func
    
# @authenticate
# def logIn():
#     if personDeets["name"] == "Mercy Nzau" and personDeets["password"] == 1234:
#         return "Logged in Succesfully"
#     else:
#         return "We si admin, na huna credentials, unadai?"
    
# print(logIn())

import time
import ipdb


def logDecorator(funcToBeDecorated):
    def addingFunctionalityFunc(*args, **kwargs):
        decoratedFuncResult = funcToBeDecorated(*args, **kwargs)
        print(f"The fuction being decorated is {funcToBeDecorated.__name__}, It is being called with arguments {args} and key word arguments {kwargs}.\n The function returned {decoratedFuncResult}")
        return decoratedFuncResult
    return addingFunctionalityFunc

@logDecorator
def add(a,b):
    return a+b


def timeDecorator(funcToBeDecorated):
    def timingFunctionalityFunc(*args,**kwargs):
        callTime = time.time()
        result = funcToBeDecorated(*args, **kwargs)
        endTime = time.time()
        totalTimeTaken = endTime-callTime
        print(f"Function {funcToBeDecorated.__name__} took {totalTimeTaken} seconds and returned {result}")
        return result
    return timingFunctionalityFunc

@timeDecorator
def multiplier(a,b):
    return a*b

# multiplier(20,30)
# multiplier(90,700)
# multiplier(3000000000,500000000)



def timeFunction(func):
    def wrapperFunc(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Fucction {func.__name__} took {end-start} seconds and returned {result}")
        return result
    return wrapperFunc

@timeFunction
def multiplier(a,b):
    return a*b

# multiplier(20,30)
# multiplier(90,700)
# multiplier(3000000000,500000000)
@logDecorator
def greeting(name):
    return f"Hello {name}"

# studentsList = ["Mercy","Javan","Bakari","Ryne"]
# mynums = [1,2,3,4]
# squares = [greeting(student) for student in studentsList]
# square_exp = (num*num for num in mynums)
# print(squares)
# print(square_exp)
# for exp in square_exp:
#     if exp == 4:
#         print(f"Target Number found. Number is: {exp}")


class User:
    def __init__(self, name, password):
        print(f"{self} initialized")
        self.name = name
        self._password = password
        pass
    def get_password(self):
        return self._password
    def set_password(self,password):
        self._password = password
        pass
    password = property(get_password,set_password)

    pass

mercy = User("Mercy Nzau",1234)
print(mercy.name)
mercy.name = "Not Mercy"
print(mercy.name)
print(mercy.password)
print(hasattr(mercy,'name'))


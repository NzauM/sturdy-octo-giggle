import ipdb

print("Mercy Nzau")
print(type(3.14))

mylist = [1,2,3,4,5,6,1,2,3,4,5,6]
mytuple = (2,3,4,5)

myset = set(mylist)
print(myset) #[]
myset.remove(3)
print(myset)

my_Students_dict = {"name":"Mercy Nzau","course":"SE"}

print(type(mylist))
print(type(mytuple))

# a function that takes in 2 numbers and returns their product/multiplies them
def multiplier(a,b):
    # ipdb.set_trace()
    return a*b

result = multiplier(20,30)
print(result)

print(not("mercy"=="mercy" or "Mercy"=="mercy"))  #true
print("mercy"=="mercy" and "mercy"=="mercy") #true
print("Mercy"!="mercy") #true


course_teacher_mapper = {
    "software engineering":"Mercy Nzau",
    "data Science":"Anthony Muiko",
    "cyber security":"Francis Kipchumba",
    "devops":"Samuel Kadima"
}

course_teacher = course_teacher_mapper.get("data Science")
# print(course_teacher)


# an authenticator which takes username and password.
# if both are correct, print("Logged In Suucessfully")
# if only one is correct, print("Check username or password")
# if both are incorrect, print("Toka hapa, wewe Mwizi")

correctusername = "Mercy"
correctpassword = 1234

def authenticator(username, password):
    if(username == correctusername and password ==  correctpassword):
        print("Logged In Suucessfully")
    elif(username == correctusername or password ==  correctpassword):
        print("Check username or password")
    else:
        print("Toka hapa, wewe Mwizi")

    return "Logged in function run"

# authenticator("Mercy","1234")


# counter = 1 #initializer
# while(counter <=5): #condition
#     print(counter) #run your statements
#     counter +=1 #change/move your initializer


# for i in range(6):
#     print(i)

mynums = [1,2,3,4]
sqare_list = [item*item for item in mynums]
print(sqare_list)

# Generator Expression
square_expression = (item*item for item in mynums)
print(square_expression)
for object in square_expression:
    print(object)




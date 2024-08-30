# decorator to log info about our add function

# define our high order function( function to receive our function)
def highOrderDecorator(funcToBeReceived):
    # wrapper function to add functionality 
    def wrapperFunc(*args, **kwargs):
        # supercharge our function
        print(f"Function Call Started. We are calling function {funcToBeReceived.__name__}")
        result = funcToBeReceived(*args, **kwargs)
        print(f"Function Call Ended, and it returned {result}")
        
        # return our function result
        # return 0
    return wrapperFunc

@highOrderDecorator
def add(a,b,c):
    print("Printed from inside add function")
    return a+b+c

add(2,3,4)


@highOrderDecorator
def subtract(num1, num2):
    print("Huku ni Subtract")
    return num1-num2

subtract(50,20)


@highOrderDecorator
def multplier(num1,num2):
    return num1*num2

multplier(20,50)


@highOrderDecorator
def greeting(name):
    return f"Hello {name}"


def testFunc():
    local_name = "Isaac Kuria"
    greeting(local_name)
    return "Done"

testFunc()

studentsList = ["Mercy","Javan","Bakari","Ryne"]

studentgreeter = [greeting(student) for student in studentsList]

print(studentgreeter, "From greeter")

student_greeting_list = [f"Hello {student}" for student in studentsList]


print(student_greeting_list)


for student in studentsList:
    greeting(student)




# greeting("Javan")
# user_name = input("What's your name?")
# greeting(user_name)


# highOrderDecorator(add(30,50))

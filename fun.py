
def greet():
    print("Hello World")

greet()   # function call


def sumtwo(a ,b):
    return a + b


sum = sumtwo(4,6)    
print(sum)



def greet(name="User"):
    print("Hello", name)

greet()
greet("Raj")



def student(name, age):
    print(name, age)

student(age=22, name="Aman")


# Multiple Return Values

def calc(a, b):
    return a+b, a-b

sum, sub = calc(10, 5)
print(sum, sub)




# Lambda Function (Short Function)



multiple = lambda a , b : a * b
print(multiple(100  , 9999))


# Built-in Functions Examples

len("Python")   # 6
type(10)        # int
max(2, 5, 8)    # 8




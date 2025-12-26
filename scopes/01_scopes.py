username = "text"

# function test(){


# }
# if True:
#     pass


def func():
    # username="Chai"
    print(username)


print(username)
func()



x = 99
def func2(y):
    z = x + y
    # print(x)
    return z

result = func2(1)
# print(result)



def f1():
    x = 88
    def f2():
        print(x)
    return f2 
myres = f1()
myres()
  


# //closer

def ch(num):
    def actual(x):
        return x ** num
    return actual


r = ch(2)
g = ch(3)

# print(r(3))
# print(g(3))



def name(f):
    def surname(l):
        return f + l
    return surname

fullname= name("raviraj")
print(fullname("choudhary"))



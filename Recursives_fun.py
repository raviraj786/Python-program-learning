
# Recursive function


# def addnum(a,b):
#     addnum(2,3)



def factorial(n):
    if n==0:
        return 1
    else:
        return  n * factorial(n-1) 



print(factorial(5))




def fc(n):
    fct = 1
    for i in range(1, n+1):
        fct *=  i  
    return fct

print(fc(5))   

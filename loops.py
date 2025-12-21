number  = [1,-2,3,-4,5,6,-7,-8,9,10]
postive_num = 0

for num in number:
    if num > 0:
        postive_num += 1
# print(postive_num)        
     

n = 10 
sum_Even = 0

for i in range(1, n+1):
    if i%2 == 0:
        # print(i)
        sum_Even += 1
# print("sum even number :", sum_Even)


# conuting postive numbers


# reversed string
input_str = "Python"
rev_str = ""

for char in input_str:
     rev_str  =   char + rev_str 
# print(rev_str)




# find the fiest non repeaded charter

str = "teeteracdacd"

for s in str:
   if str.count(s) == 1:
    #    print("char is" , s)
       break



# find factorial calculalaor
# 5 = 5*4*3*2*1

number  = 5
fectorial = 1

while number > 0:
    fectorial *= number
    number -= 1
    
# print( "fectorial value number of:",fectorial)






# validate number

# while True:
#     number=int(input("enter value b/w 1 & 10"))
#     if 1<= number <= 10:
#         print("ok")
#         break
#     else:
#         print("invalid number try")




# for num in range(20):
#     if num % 2 == 0:
#         print(num)


# prime num

number  = 20

is_prime = True 

if number > 1:
    for i in range( 2 , number):
        if(number % i) == 0:
         is_prime =  False
         break
          
# print(number  , ":" , is_prime , ":prime number")

items  = ["apple" , "banna" , "orange" , "apple" , "mango"]

unque_item = set()

for item in items:
    if item in unque_item:
        print("Dulpicate" , item)
        break
    unque_item.add(item)


print(unque_item)








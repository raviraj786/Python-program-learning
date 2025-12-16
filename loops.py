

# age = 100

# if age < 13:
#     print('child')
# elif age < 20:
#     print('teenagger')
# elif age  < 60:
#     print("adult") 
# else:
#     print("senior")



age = 17
day = "wednesday"
price = 12 if age >= 18 else 8
if day == "wednesday":
    price = price - 2
# print("Ticket price for you is $",price)



# Grade calculater
score = 30

if score >= 101:
    print("please verify your grade again")
    exit()
elif score >= 90:
    gread = 'A'
elif score >=80:
    gread = 'B'
elif score >= 70:
     gread = 'c'
elif score >= 60:
     gread = 'D'
else:
    gread = "F"

# print("Grade :",gread) 



weather  = "sunny"

if weather == "sunny":
    activity = "go for a walk"
elif weather == "Rainy":
    activity = "read a book"
elif weather == "snowy":
     activity = "build a snowmn"
# print(activity )            







# km = 20

# if km <= 3:
#     print("walk")
# elif km <=15:
#     print("car")
# else:
#     print("no idea")      




# coffee customaize


custmer_order = "samll"
extra_short = True

if extra_short:
    coffee = custmer_order  + "coffee order"  
else:
    coffee = custmer_order + "coffee order"  

# print(coffee)


# pet food recommendation


pet_age = 1
if pet_age < 2:
   petfood = "Dog puppy food"
elif pet_age > 5:
     petfood = "senior cat food"
else:
    petfood = "no find"     
# print(petfood)


password = "secure2p@s"

if len(password) < 6:
    strength = "week"
elif len(password) <=6:
    strength = "medium"
else:
    strength = "strong"  
# print("password strenght is:" , strength)         


# leap year

year = 2000

if (year % 400 == 0) or(year % 4 == 0 and year % 100 !=0):
            print(year ,": leap year")
else:
     print(year , "not leap year")












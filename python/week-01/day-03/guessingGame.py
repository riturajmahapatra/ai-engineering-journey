import random
print(5 > 3) # True

print(5 < 3) # False

print(5 == 5) # True

print(5 != 5) # False

print(5 >= 5) # True

print(5 <= 4) # True

age = 29
print(10*'-')

print(age > 18) # True

print(age < 18) # False

print(age == 29) # True

print(age != 30) # True

print(10*'-')

if True:
    print("Hello") # IndentationError if the space is removed

print("World")

print(10*'-')

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor") # prints Minor

print(10*'-')

marks = 72

if marks >= 90:
    print("A")

elif marks >= 75:
    print("B")

elif marks >= 50: # prints C cuz marks =72 
    print("C")

else:
    print("Fail")
####################### Mini Proj  1  
print(10*'-')

weight = int(input('weight: '))
height = int(input('height: '))
height_mts = height/100 # mts conversion

bmi = weight/(height_mts*height_mts)

if bmi < 18.5:
    print('Category : Underweight')
elif 18.5 >= bmi < 24.9 :  
    print('Category : Healthy') 
elif 25>= bmi < 29.9 :  
    print('Category : Overweight') 
else : print('Category : Obese')

####################### Main Proj #######################
print(10*'-')

computer = random.randint(1,10)
user = int(input('Enter a integer value: '))


while(computer != user): # use a counter for managing the respose ands attempts
    user = int(input('Enter a integer value: '))
    if computer>user:
        print('Too Low')
    elif computer==user:
        print("You are Correct")    
    else: print("Too High")

age = 20

if age > 18:
    print("A") # A because pyton is top down approach whatever is first and is correct will print 

if age > 15:
    print("B")

else:
    print("C")
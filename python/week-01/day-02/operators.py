a = 20
b = 3

print(a + b) #23
print(a - b) #17
print(a * b) #60
print(a / b) #6.01
print(a // b) #6
print(a % b) #2
print(a ** b)  # 8000

# lesson2 type conversions
age = int(input('input age:')) # parse int before the input to get the type int as age is int not 'str' as that is what we get in input as it takes str

print(type(age))
age2 = int(input("Age: "))

print(age2 + 1)

# floats 
name = input('Name: ')
height = float(input("Height in cms: "))
print((f'{name} your height is {height} cm'))
height_in_mts = height/100

# String methods
print(name)
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
city = '  de lhi  '
print(city.strip())

challenge = '      ai engineering   '
print(challenge.capitalize().strip())
print(challenge.title().strip()) # challenge complete

weight = float(input('Enter your weight (kgs): '))
bmi = weight / (height_in_mts * height_in_mts)

print('=' * 30) # instead do this print("=" * 30)
print('BMI REPORT')
print(30*'=')
print(f''' 
    Name : {name}
    
    Weight : {weight} kgs
      
    Height : {height} cm
        
    BMI : {bmi}
      
      
      ''')

if bmi < 18.5:
    print('Underweight')
elif 18.5 >= bmi < 24.9 :  
    print('Healthy') 
elif 25>= bmi < 29.9 :  
    print('Overweight') 
else : print('Obese')

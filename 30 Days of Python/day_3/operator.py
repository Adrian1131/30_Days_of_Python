#booleans 
print(True)
print(False)

#Arithmetic Operators
#Numbers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

a = 3 
b = 2

# Arithmetic Operators
total = a + b 
diff = a - b
product = a * b
division = a / b
remainder = a % b 
floor_division = a // b 
exponential = a ** b 

print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total) # always remember to use labels when printing
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
print('\n')
print('=== Addition, Subtraction, Multiplication, Division, Modulus ===')
print('\n')
num_one = 3 
num_two = 2 

#Arithmetic Operations
total = num_one + num_two
diff = num_two - num_two
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

#Calculating the area of a circle 
radius = 10 
area_of_circle = 3.14 * radius ** 2
print('Area of Circle: ', area_of_circle)

#Calculating area of a rectangle
length = 10 
width = 20
area_of_rectangle = length * width
print('Area of Rectangle: ', area_of_rectangle)

#Calculating weight of an object
mass = 75 
gravity = 9.81
weight = mass * gravity
print('weight', 'N') #adding unit to the weight

# Calculating the density of liquid
mass = 75 # in kg
volume = 0.075
density = mass / volume

# Comparison Operators
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('A in Adrian', 'A' in 'Adrian')
print('D in Adrian', 'D' in 'Adrian')
print('coding' in 'coding for all')
print('a in an: ', 'a' in 'an')
print('4 is 2 ** 2', 4 is 2 ** 2)

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

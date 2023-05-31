#1
age = 22

#2
height = float(73)

#3
c_number = complex(3,4)

#4
print('Area of the triangle: ',int(input('Base:')) * int(input('Height: ')))

#5
print('Perimeter of Triangle: ',int(input('a: ')), int(input('b: ')), int(input('c: ')))

#6
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
print('Area: ', length * width)
print('Perimeter: ', 2 * (length + width))

#7
radius = int(input('Enter the radius: '))
print('Area: ', 3.14 * radius * radius)
print('Circumference: ', 2 * 3.14 * radius)

#8
print('x intercept: ', 1)
print('y intercept', 4)
print('slope ', 2)

#9
x1, x2, y1, y2 = 2, 6, 2, 10
print('Distance: ')
print('{0:.2f}'.format(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)) #0:.2f rounds up 2 decimals
print('Slope: ')
print((y2 - y1) / (x2 - x1))

#10
print(2 if 2 < (y2 - y1) else (y2 - y1) / (x2 - x1))

#11
for x in range (0, 10):
    print(x ** 2 + 6 * x + 9)
    print(3, -3, 'is where y meets 0')

#12
print(not len('python') == len('dragon'))

#13
print('on' in 'python' and 'on' in 'dragon')

#14
print('jargon' in 'is jargon in the sentence')

#15
print('on' not in 'python' and 'on' not in 'dragon')

#16
print(str(float(len('python'))))

#17
num = int(input("Enter a number: "))

if (num % 2) == 0:
    print("{0} is an even number".format(num))
else:
    print("{0} is an odd number".format(num))

# 18
number = int(input('Enter number:'))
print("Even" if number % 2 == 0 else "Odd")

# 19
print(type('10') == type(10))

# 20
print(int('9.8') == 10)

# 21
hours = int(input('Enter hours:'))
rph = int(input('Enter rate per hour:'))
print("Weekly Earning:", hours * rph)

# 22
years = int(input('Enter years:'))
print(years * 365 * 24 * 60 * 60 * 60)

# 23
for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)
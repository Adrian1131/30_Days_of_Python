#1
s1 = 'Thirty'
s2 = 'Days'
s3 = 'Of'
s4 = 'Python'

print(s1 + s2 + s3 + s4)

#2
print(' '.join(['Coding', 'for', 'All']))

#3
company = 'Coding for All'
print(company)

#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[7:]) #slices string, ends at the 6th index

#10
print(company[company.index('Coding'):8])
print(company[company.find('Coding'):8])

#11
print(company.replace('Coding','Not'))

#12
print('Python for Everyone'.replace('Everyone', 'All'))

#13
print(company.split())

#14
print('Facebook', 'Google', 'Microsoft', 'IBM', 'Oracle', 'Amazon'.split(','))

#15
print(company[0])

#16
print(len(company[-1]))

#17
print(company[10])

#18
words = 'Python for Everyone'.split()
print(words[0][0] + words[1][0] + words[1][1]) #prints acronym

#19
acro = 'Coding for All'
print(acro[0][0] + words[1][0] + words[2][0])

#20
print('Coding For All'.index('C'))

#21
print('Coding For All'.index('F'))

#22
print('Coding For All'.rfind('i'))

#23
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

#24
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

#25
print()

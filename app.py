from multiprocessing.sharedctypes import typecode_to_type

print("I am Lubna Mulla")
print('0----')
print(' ||||')
print('*' * 10)
price = 10
price=20
rating=4.9
name='lubna'
is_published=True
print(price)
full_name='John Smith'
age=20
is_new=True
#Input function is used to take input from the user
#name=input('what is your name? ')
#Favorite_color=input('what is your favorite color? ')
#print( name + ' likes ' + Favorite_color)
#Type conversion there are function which convert strings to Int(). Float(), Bool()
#Birth_year=input('Birth year: ')
#print(type(Birth_year))
#age=2025- int(Birth_year)
#print(age)
#print(type(age))
#weight_lbs=input('weight (lbs): ')
#weight_kg= int(weight_lbs) * 0.4535
#print(weight_kg)
#Strings
course=" Python's course for beginners"
#print(course)
course='Python for "beginners"'
#print(course)
course='Python for beginners'
# find  0123 index of character is we pass 0 it will return p, if we pass -ve value -1 it will return last character from the string that is S n so on
print(course[0])
print(course[1])
print(course[-1])
print(course[-2])
#here python will interpreter will return characters starting from index 0 all the way to index 3 but excludes the character 3
print(course[0:3])
print(course[0:])
print(course[:5])
print(course[:])
name='jennifer'
print(name[1:-1])

#formatted strings
first='john'
last='smith'
message=first + '[' + last + ']  is a coder'
print(message)
# formatted string prefix with f and use curly brackets its easy to visualise the output
msg=f'{first}[{last}] is a coder'
print(msg)
#String Methods
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('P'))
print(course.find('p', 1))
print(course.find('O'))
print(course.find('o'))
print(course.find('Beginners'))
print(course.find('beginners'))
print(course.replace('beginners', 'Absolute Beginners'))
print(course.replace('P','J'))
print('python' in course)
print('Python' in course)
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10**3)
#Augmented assignment operator
x=10
x=x+3
print(x)
y=10
y+=3
print(y)
y-=3
print(y)
#Precedence of operators(highest to lowest)
#(),**,/ or *,- or +
x=10+3*2
print(x)
x=(2+3)*10-3
print(x)

#Math Functions
x=2.9
print(round(x))
#absolute function(abs) always returns +ve value
print(abs(-2.9))
#module is a separate file with some reusable code.We use this module to organise code into different file.
import math
print(math.ceil(2.9))
print(math.floor(2.9))
print(math.fabs(x))

#if statements
is_hot:bool=True
print(is_hot)
is_cold:bool=False
if is_hot:
    print("It's hot day")
    print("drink plenty of water")
elif is_cold:
    print("It's cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")

print("enjoy your day")

#exercise2:
price=100000
has_good_credit=True
if has_good_credit:
   down_payment= 0.1 * price
else:
   down_payment= 0.2 * price

print(f"Down_payment: ${down_payment}")


# This program generates a multiplication table for a number entered by the user.

tab_number = int(input("Enter the number of your choice to print the multiplication table: "))

# Print the header for the multiplication table
print("The Multiplication Table of:", tab_number)

# Use a for loop to iterate 10 times and print the table
for count in range(1, 11):
    print(tab_number, 'x', count, '=', tab_number * count)

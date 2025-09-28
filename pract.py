print('Hello, Python!')
print("Hello, Python!")
print('''Hello, Python!''')
print('"Hello, Python"')
print("'Hello, Python'")
#Python Add Two Numbers Program
number1 = 5
number2 = 4
# Add two numbers
sum = number1 + number2
# Display the sum of the two numbers
print('The sum of the two numbers is:', sum)

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = num1 + num2
print('The sum of the numbers is', sum)
#Python input() function always converts the user input into a string. Whether you enter an int or float value it will consider it as a string. We need to convert it into number using int() or float() functions. See the below example.
sum = int(num1) + int(num2)
print('The sum of the numbers is', sum)

# Read the input numbers from users
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

# Converting and adding two numbers using int() & float() functions
sum = int(num1) + int(num2)

# Subtracting the two numbers
sub = int(num1) - int(num2)

# Multiplying two numbers
mul = float(num1) * float(num2)

#Dividing two numbers
div = float(num1) / float(num2)

# Displaying the results of arithmetic operations
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The subtration of {0} and {1} is {2}'.format(num1, num2, sub))
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))
print('The division of {0} and {1} is {2}'.format(num1, num2, div))

# Python program to check if a number is odd or even

# To get the input from user
num1 = input("Enter a number: ")

# Checking whether the entered number is odd or even
if (int(num1) % 2) == 0:
    print("{0} is Even number".format(num1))
else:
    print("{0} is Odd number".format(num1))


#To read the input value from the user
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

#Finding the maximum value using Python max() funtion
maximum = max(int(num1), int(num2))

#Displaying the maximum number
print("The maximum number is: ",maximum)

# Function to check prime number
def PrimeChecking(num):
    # Condition to check given number is more than 1
    if num > 1:
        # For look to iterate over the given number
        for i in range(2, int(num/2) + 1):
            # Condition to check if the given number is divisible
            if (num % i) == 0:
                #If divisible by any number it's not a prime number
                print("The number ",num, "is not a prime number")
                break
        # Else print it as a prime number
        else:
            print("The number ",num, "is a prime number")
    # If the given number is 1
    else:
        print("The number ",num, "is not a prime number")
# Input function to take the number from user
num = int(input("Enter a number to check prime or not: "))
# To print the result, whether a given number is prime or not
PrimeChecking(num)

#Python program to find factorial of a given number

#importing the math function
import math

#Defining the factorial() function to find factorial
def factorial(num):
	return(math.factorial(num))


# Input function to get the number from user
num = int(input('Please enter a number to find the factorial: '))

#Printing the factorial of the given number
print("The factorial of the given number", num, "is",
	factorial(num))

# Input function to get the input from the user
n = float(input('Enter a number: '))

#Formula to calculate the square root of the number
n_sqrt = n ** 0.5

#Printing the calculated square root of the given number
print('The square root of {0} is {1}'.format(n ,n_sqrt))

# Python Program to find the area of a triangle

# Get the 3 sides of a triangle from the user
s1 = float(input('Enter first side value: '))
s2 = float(input('Enter second side value:'))
s3 = float(input('Enter third-side value:'))

#Calculating the semi-perimeter of a triangle
sp = (s1 + s2 + s3) / 2

#Calculating the area of a triangle
area = (sp*(sp-s1)*(sp-2)*(sp-s3)) ** 0.5

#Printing the area of the triangle
print('The area of the triangle is: ', area)

# python program to check armstrong number

#Taking the input from user to check armstrong number
num=int(input("Enter the number to check armstrong number: "))

#Assigning the num value to arms
arms = num

#Finding the length of the number
length = len(str(num))
sum1 = 0

#Iterating the values to check armstrong number
while num != 0:
	rem = num % 10
	sum1 = sum1+(rem**length)
	num = num//10

#Printing the result whether the given number is armstrong number or not
if arms == sum1:
	print("The given number", arms, "is armstrong number")
else:
	print("The given number", arms, "is not an armstrong number")


# Python program to check whether the given year is leap year or not

# Function implementation to check leap year
def LeapYear(Year):
    # Condition to check if the given year is leap year or not
    if ((Year % 400 == 0) or
            (Year % 100 != 0) and
            (Year % 4 == 0)):
        print("The given Year is a leap year");
        # Else it is not a leap year
    else:
        print("The given Year is not a leap year")
        # Taking an input year from user


Year = int(input("Enter the year to check whether a leap year or not: "))
# Printing the leap year result
LeapYear(Year)

# Python program to check prime number

# This program checks if a number entered by the user is a prime number.

# Get the number from the user.
prime_num = int(input("Enter a number to check whether it is prime or not: "))

# A prime number is a natural number greater than 1.
if prime_num > 1:
    # We check for factors from 2 up to the square root of the number.
    # This is more efficient than checking up to prime_num / 2.
    for i in range(2, int(prime_num**0.5) + 1):
        # If the number is divisible by any other number, it's not prime.
        if (prime_num % i) == 0:
            print(prime_num, "is not a prime number")
            break  # We can stop checking once a factor is found.
    # The 'else' block for the 'for' loop runs only if the loop
    # completes without a 'break' statement, meaning no factors were found.
    else:
        print(prime_num, "is a prime number")
else:
    # Numbers less than or equal to 1 are not considered prime.
    print(prime_num, "is not a prime number")

    # Python program to display multiplication table

    # This program generates a multiplication table for a number entered by the user.

    tab_number = int(input("Enter the number of your choice to print the multiplication table: "))

    # Print the header for the multiplication table
    print("The Multiplication Table of:", tab_number)

    # Use a for loop to iterate 10 times and print the table
    for count in range(1, 11):
        print(tab_number, 'x', count, '=', tab_number * count)

        # Take inputs from the user to swap the two variables
        num1 = input('Enter the first variable: ')
        num2 = input('Enter the second variable: ')

        # Printing the numbers before swap
        print('The value of num1 before swapping: {}'.format(num1))
        print('The value of num2 before swapping: {}'.format(num2))

        # Use temporary variable and swap the values lubna
        temp = num1
        num1 = num2
        num2 = temp

        # Printing the numbers after swap
        print('The value of num1 after swapping: {}'.format(num1))
        print('The value of num2 after swapping: {}'.format(num2))

print( "my name is Lubna")





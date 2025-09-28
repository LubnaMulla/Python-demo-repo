# Take inputs from the user to swap the two variables
num1 = input('Enter the first variable: ')
num2 = input('Enter the second variable: ')

#Printing the numbers before swap
print('The value of num1 before swapping: {}'.format(num1))
print('The value of num2 before swapping: {}'.format(num2))

#Use temporary variable and swap the values
temp = num1
num1 = num2
num2 = temp

#Printing the numbers after swap
print('The value of num1 after swapping: {}'.format(num1))
print('The value of num2 after swapping: {}'.format(num2))

# Prime number program
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

def main():
    limit = 100
    primes = find_primes(limit)
    print(f"Prime numbers up to {limit}: {primes}")

if __name__ == "__main__":
    main()

    # Factorial
    def factorial(n):
        """Calculates the factorial of a non-negative integer."""
        if n < 0 or not isinstance(n, int):
            return "Error: Factorial is only defined for non-negative integers."

        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


    # Example usage:
    if __name__ == "__main__":
        num = 5
        print(f"The factorial of {num} is: {factorial(num)}")

        num = 0
        print(f"The factorial of {num} is: {factorial(num)}")

        num = -3
        print(f"The factorial of {num} is: {factorial(num)}")

# Palindrome
import re

def is_palindrome(text):
    """Checks if a string is a palindrome, ignoring non-alphanumeric characters."""
    cleaned = re.sub(r'[^a-z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]

# Example usage:
word = "A man, a plan, a canal: Panama"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")

#Fibonacci
def fibonacci(n):
    """Generates the first n Fibonacci numbers."""
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Example usage:
print(f"The first 10 Fibonacci numbers are: {fibonacci(10)}")

#Armstrong number
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

#sum of digits
def sum_of_digits(number):
    """
    Calculates the sum of the digits of a number.
    Handles both positive and negative integers.
    """
    # Take the absolute value to handle negative numbers
    number = abs(number)

    total_sum = 0
    # Convert the number to a string to easily iterate through each digit
    for digit_char in str(number):
        # Convert each character back to an integer and add to the sum
        total_sum += int(digit_char)

    return total_sum

#print list of colors in ascending or descending order
# Main part of the script
if __name__ == "__main__":
    try:
        # Prompt the user to enter a number
        user_input = input("Enter a number to find the sum of its digits: ")

        # Convert the user's input to an integer
        num = int(user_input)

        # Call the function to get the result
        result = sum_of_digits(num)

        # Print the final result to the user
        print(f"The sum of the digits of {num} is: {result}")

    except ValueError:
        # Handle cases where the user enters non-integer input (e.g., text or a decimal)
        print("Invalid input. Please enter a whole number.")


def main():
    """
    Main function to get a list of colors from the user and print them
    in ascending and descending order.
    """
    try:
        # Prompt the user for input. The input is expected to be a
        # comma-separated string of colors.
        color_input = input("Enter a list of colors, separated by commas (e.g., 'red, green, blue'): ")

        # Split the input string into a list of colors.
        # .strip() is used to remove leading/trailing whitespace from each color name.
        colors = [color.strip() for color in color_input.split(',')]

        # Check if the list is empty after stripping whitespace.
        if not any(colors):
            print("No colors were entered. Please try again.")
            return

        # Sort the list in ascending (alphabetical) order.
        colors.sort()
        print("\nColors in ascending order:")
        for color in colors:
            print(f"- {color}")

        # Sort the list in descending order.
        colors.sort(reverse=True)
        print("\nColors in descending order:")
        for color in colors:
            print(f"- {color}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # This ensures the main function is called when the script is executed.


if __name__ == "__main__":
    main()


    def reverse_string():
        """
        Prompts the user for a string and prints it in reverse.
        """
        # Get user input
        user_input = input("Please enter a string to reverse: ")

        # Reverse the string using slicing
        reversed_string = user_input[::-1]

        # Print the reversed string
        print(f"The reversed string is: {reversed_string}")



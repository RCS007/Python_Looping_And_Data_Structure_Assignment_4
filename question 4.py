# Question 4

# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a
# prime number is a number that has no divisors.).

# Function to check if a number is prime
def is_prime(number):
    # Numbers less than or equal to 1 are not prime
    if number <= 1:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:  # If the number is divisible by i, it's not prime
            return False
    return True

# Ask the user for a number
user_input = int(input("Enter a number: "))

# Check if the number is prime and display the result
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")

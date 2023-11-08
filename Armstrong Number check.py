def is_armstrong_number(number):
    # Convert the number to a string to access individual digits
    num_str = str(number)

    # Calculate the order (number of digits) of the given number
    order = len(num_str)

    # Initialize a variable to store the sum of cubes of each digit
    sum_of_cubes = 0

    # Loop through each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer
        digit_int = int(digit)

        # Calculate the cube of the digit and add it to the sum
        cube = digit_int ** order
        sum_of_cubes += cube

    # Check if the sum of cubes is equal to the original number
    return sum_of_cubes == number

# Get input from the user
num = int(input("Enter a number: "))

if num < 0:
    print("Negative numbers cannot be Armstrong numbers.")
elif is_armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

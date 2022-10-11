# Name: Robert Savoie
# Date: Oct 11/2022
# File Type: .py
# Description: Takes a list of numbers and validates that they're numbers.
#              It then finds the lowest number and prints it using the minimum_number function.

def minimum_number(vals):
    # Creates a reference value
    minimum = vals[0]
    for value in vals:
        # For each value in the list it checks if it's smaller than the reference.
        # If it is it sets the reference to the new value.
        if value < minimum:
            minimum = value
    return minimum


# Establish while loop
cont = True
while cont:
    numbers = input("Please enter a set of numbers: ").split(" ")
    try:
        numbers = [int(number) for number in numbers]
        # If no number input continue the loop else break loop
        if len(numbers) == 0:
            break
        else:
            cont = False
    # Exception handling catch
    except ValueError:
        print("Error Message: Exception Handling")

# Calls function to find minimum number and prints it.
print(minimum_number(numbers))

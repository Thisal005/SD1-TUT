# Input a non-negative integer from the user
num = int(input("Enter a non-negative integer: "))

# Initialize the factorial to 1 and the loop counter x to 1
factorial = 1
x = 1

# Calculate the factorial using a while loop
while x <= num:
    factorial *= x
    x += 1

# Display the factorial
print("The factorial of", num, "is", factorial)

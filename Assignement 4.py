# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# Adding a prompt when the input given is invalid
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Ask user to input 3 numbers.
num1 = get_float_input  ( "Enter the 1st number: ")
num2 = get_float_input  ( "Enter the 2nd number: ")
num3 = get_float_input  ( "Enter the 3rd number: ")

# Find and print the biggest number using only if-else statement

# Compare the numbers to find the biggest number
if num1 >= num2 and num1 >= num3:
    biggest = num1
if num2 >= num1 and num2 >= num3:
    biggest = num2
else:
    biggest = num3

# Print the biggest number ( make it goood)
print("\n╔════════════════════════════════╗")
print("║          YOU ENTERED:          ║")
print("║════════════════════════════════║")
print("║        {:.2f}, {:.2f}, {:.2f}        ║".format(num1, num2, num3))
print("╠════════════════════════════════╣")
print("║  THE BIGGEST NUMBER IS: {:.2f}   ║".format(biggest))
print("╚════════════════════════════════╝")
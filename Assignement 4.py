# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement

# Ask user to input 3 numbers.
num1 = float (input ( "Enter the 1st number: "))
num2 = float (input ( "Enter the 2nd number: "))
num3 = float (input ( "Enter the 3rd number: "))

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
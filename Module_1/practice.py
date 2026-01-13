# first code every beginner should write
print("Hello, World!") # This line prints the classic greeting to the console


# data types and variable assignment
# integer
age = 25  # Assigning the integer value 25 to the variable age
# float
height = 5.9  # Assigning the float value 5.9 to the variable height
# string
name = "Alice"  # Assigning the string "Alice" to the variable name
# boolean
is_student = True  # Assigning the boolean value True to the variable is_student
# printing the variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# variable assignment
x = 10  # Assigning the integer value 10 to the variable x
y = 5   # Assigning the integer value 5 to the variable y


# simple arithmetic operation
sum_xy = x + y  # Calculating the sum of x and y and storing it in sum_xy
print("The sum of", x, "and", y, "is:", sum_xy)


# conditional statement
if sum_xy > 10:
    print("The sum is greater than 10.")
else:
    print("The sum is 10 or less.")


# function definition
def greet(name):
    """Function to greet a person with their name."""
    return "Hello, " + name + "!"
# calling the function
greeting_message = greet("Alice")
print(greeting_message)


# loop example
for i in range(3):
    print("This is loop iteration number:", i + 1)
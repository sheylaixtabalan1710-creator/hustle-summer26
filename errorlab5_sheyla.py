#Snippet 1
x = 10
y = 0
divisor = 0
if divisor == 0:
     print("Cannot divide by zero.")
#PREDICT: the code will break because y = 0 and you can't divide by 0.
#FIX: I added an if statement.
#Snippet 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
#PREDICT: the code will break because the index is out of range.
#FIX: I took away the + 1 and left only the i so it will print the numbers in the list.
#Snippet 3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))
#PREDICT: the code will break because there is a syntax error.
#FIX: I added a colon and I indented 2 lines.
#Snippet 4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))
#PREDICT: the code will break where it says if number % 2 == 0.
#FIX: I added a colon and indented some lines.
#Snippet 5
for i in range(5):
    print(i)
#PREDICT: the code will break where it says for i in range(5).
#FIX: I added a colon and indented the print.
#Snippet 6
def greet(name):
    return "Hello, " + name
print(greet("Alice"))
#PREDICT: The code will break on the hello name line.
#FIX: I added a colon and indented the return statement.
#Snippet 7
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)
#PREDICT: The code will break on the total += number line.
#FIX: I indented the total += number line.
#Snippet 8
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
#PREDICT: The code will break on the return n * factorial(n + 1) line.
#FIX: I changed the + 1 to - 1 so it will calculate the factorial correctly.
#Snippet 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
#PREDICT: The code will break on the if name== Alice line.
#FIX: I added a == before bob.
#Snippet 10
def divide_numbers(x, y):
    if y == 0:
        return("Error: Cannot divide by zero.")

    else:
        return x / y
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))
#PREDICT:The code will break because you cant divide by 0.
#FIX: I added an if and else statement.
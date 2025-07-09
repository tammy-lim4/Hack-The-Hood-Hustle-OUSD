# Debugging Activity, Tammy Lim

# Code Snippet 1:
x = 10
y = 3
result = x / y  # Zero division error, fixed by changing: y = 3
print("Result:", result)

# Code Snippet 2:
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])  # Logic error, fixed by removing the +1 in i+1

# Code Snippet 3:
def calculate_area(radius):  # Syntax error fixed by adding colon
    area = 3.14 * radius ** 2
    return area
radius = 5
print(calculate_area(radius))

# Code Snippet 4:
def is_even(number):
    if number % 2 == 0:  # Syntax error fixed by adding colon
        return True
    else:  # Syntax error fixed by adding colon
        return False
print(is_even(4))
print(is_even(7))

# Code Snippet 5:
for i in range(5):  # Syntax error fixed by adding colon
    print(i)

# Code Snippet 6:
def greet(name):
   return 'Hello ' + name # Syntax error fixed by adding +
print(greet("Alice"))

# Code Snippet 7:
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number # Syntax error fixed by adding indent
print("Sum of numbers:", sum)

# Code Snippet 8:
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1) # Logic error fixed by changing n+1 to n-1
 
print(factorial(5))

# Code Snippet 9:
name = input("Enter your name: ")
if name == "Alice" or  name == "Bob": # Logic error fixed by adding 'name ==' to "bob"
   print("Hello, " + name)
else:
   print("Hello, stranger!")

# Code Snippet 10:
def divide_numbers(x, y):
   result = x / y
   return result
num1 = 10
num2 = 2 # Zero division error, fixed by changing num2 to 2
print(divide_numbers(num1, num2))



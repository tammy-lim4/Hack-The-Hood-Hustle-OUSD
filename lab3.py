# Lab 3

# Task 1: Working With Strings

food = "chicken alfredo"
print(food[0:3])  # Print First 3 Characters
print(food[-3:])  # Print Last 3 Characters
First_Last = food[0] + food[-1]  # Combine First & Last Character
print(First_Last)
food_list = food.split()  # Split string into a list
print(food_list)
joined_food = ' '.join(food_list)  # Join list of words into a single string
print(joined_food)

# Task 2: Working With Lists

number_list = [1, 2, 3, 4, 5, 6, 7]
number_list.append(8)  # Add a new integer at the end of the list
number_list.insert(3, 3.5)  # Insert an element in the 3rd index
number_list.pop(-1)  # Remove the last integer in the list
number_list.remove(2)  # Remove the second integer
print(number_list)  # Print the list
print(number_list[0:3])  # Print first 3 characters
print(number_list[-3:])  # Print last 3 characters

# Task 3: Working With Dictionaries

books = {'Dr. Seuss': 'Cat in the Hat', 'Jeff Kinney': 'Diary of a Wimpy Kid',
         'Jeff Brown': 'Flat Stanley', 'Suzanne Collins': 'The Hunger Games'} # Variable with 4 key-value pairs
keys = books.keys()  # List of all keys in dictionary
print(keys)
values = books.values()  # List of all values in dictionary
print(values)
x = books.get("Suzanne Collins") # Retrieve the value for a specific key in the dictionary
print(x)
books.pop("Jeff Brown")  # Remove 3rd key-value pair from dictionary
print(books)
del books["Dr. Seuss"]  # Remove 1st key-value pair from dictionary
print(books)
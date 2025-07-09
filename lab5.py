## Lab 5, Tammy Lim

# Task 1 Cat Greeting Function
def cat_greeting(word):
    print(f"cat says {word}")
    import random
    age = random.randint(1,100)
    print("The cat's age is:", age , 'years old')
    return
cat_greeting('meow')

# Task 2 Superhero Power Function (Fixed Output)
def generate_superhero_power1():
    name = 'John'
    power = 'Flying'
    print(name, 'has the power of', power)
generate_superhero_power1()

# Task 3 Superhero Power Function with Return
def generate_superhero_power2():
    import random
    random_power_index = random.randint(0,5)
    power_list = ['super strength','flight','teleportation','invisiblity','telekinesis','shape shifting']
    power = power_list[random_power_index]
    return power
print(f'Your random superhero power is: {generate_superhero_power2()}')

#Task 4 Superhero Power Function with Arguments
def generate_superhero_power3(user_name,user_power):
    sentence = f'{user_name} has the power of: {user_power}!'
    return sentence
print(generate_superhero_power3('Tammy','strength'))

# Task 5 Looping through Greetings
def cat_greetings_loop(cat_says):
    for i in range(5):
        print(f'The cat says: {cat_says}')
cat_greetings_loop('Meow!')

# Task 6 Superhero Power Function with Multiple Powers
def generate_multiple_powers(power_list):
    for i in power_list:
        print(f'Your power is: {i}')
generate_multiple_powers(["Flight","Super Strength", "Telekinesis","Invisibility","Teleportation","Energy Manipulation","Super Speed"])
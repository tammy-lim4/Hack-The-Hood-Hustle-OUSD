# Task 1 Checking Voting Eligibility Repeatedly
checking = "yes"

while checking == "yes":
    print("What is your age: ")
    user_input = input()
    if int(user_input) >= 18:
        print("Yes, you can vote")
    else:
        print("You cannot vote")

    print("Would you like to check another age?")
    user_input2 = input()
    checking = user_input2

# Task 2 Checking Multiple Numbers for Positivity or Negativity
List1 = [3, -1, 0, 6, -4]

for x in List1:
    if x > 0:
        print("The value is positive")
    elif x < 0:
        print("The value is negative")
    else:
        print("The number is zero")

# Task 3 Collecting Blocks in Minecraft
Inventory = ['cobblestone', 'coal', 'dirt', 'diamond', 'netherite', 'gold', 'iron']
List_length = len(Inventory)

for i in range(List_length):
    current_item = Inventory[i]

    print(f"You found {current_item}.")

    if current_item == 'diamond':
        print("Jackpot! You found a diamond")

# Bonus Challenge
while True:
    print('To check voting eligibity, please enter your age, or type STOP to exit.')
    user_input3 = input()
    if user_input3 == 'STOP':
        print('Program will stop now.')
        break

    if int(user_input3) >= 18:
        print('You are eligible to vote')
    elif int(user_input3) < 18:
        print('You are not eligible to vote')
    else:
        print('Program will stop now')

    print('Would you like to check another age?')
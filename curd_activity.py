# CRUD Activity - Tammy Lim


# Step 1

cookbook = []

# Step 2

def create(recipe):
    cookbook.append(recipe)
    print(f"Added {recipe} to cookbook")
    return cookbook
# print(create('Apple Pie'))

# Step 3

def read(index_number):
    full_index = len(cookbook)
    if 0 <= index_number < full_index:
        item = cookbook[index_number]
        print(item)
    else:
        print('The index number is out of range')
# print(read(0))

# Step 4

def update(index_number, newitem):
    full_index = len(cookbook)
    if 0 <= index_number < full_index:
        cookbook.pop(index_number)
        cookbook.insert(index_number, newitem)
        print(f'Your updated cookbook is:', cookbook)
    else:
        print('The index number is out of range')

# Step 5

def destroy(index_number):
    full_index = len(cookbook)
    if 0 <= index_number < full_index:
        removed_item = cookbook.pop(index_number)
        print(f'Removed', removed_item)
        print(f'Your updated cookbook is:', cookbook)
    else:
        print('The index number is out of range')


# Step 6

def list_all_recipes():
    for recipe in cookbook:
        print(recipe)

# Step 7

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input(
                "Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()

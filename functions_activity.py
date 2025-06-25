menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

# Step II

def total_price(item1, item2):
    total_sum = menu[item1]+menu[item2]
    return total_sum

#print(total_price('Pizza','Burger'))

#Step III

def price_difference(item1, item2):
    total_difference = abs(menu[item1]-menu[item2])
    return total_difference
#print(price_difference('Cheese', 'Hot dog'))

#Step IV

def inflation(number, item1):
    inflated_price = number * menu[item1]
    menu[item1] = inflated_price
    return menu
#print(inflation(3,'Cheese'))

#Step V

def deflation(item1, number):
    deflated_price = menu[item1] / number
    menu[item1] = deflated_price
    return menu
#print(deflation('Pizza',2))

#Step VI

def future_price(item1,inflationrate,years):
    future_amount = menu[item1] * ((1+inflationrate)**years)
    menu[item1] = future_amount
    return menu
print(future_price('Pizza',0.03,3))
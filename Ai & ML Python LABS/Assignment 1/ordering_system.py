menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}
def show_menu():
    print("MENU")
for item_no,info in menu.items():    
    print(f"{item_no}. {info['name']} / ${info['price']}")

def choose_item():
    order_list = []
    for _ in range(3):
        try:
            items = int(input("What would you like to order?: "))
            order_list.append(menu[items])
        except (ValueError, KeyError):
            print("Invalid Item_No!! Please Enter a Valid Item_No")
    return order_list
    
    
def calculate_subtotal(order_list):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME] 
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    subtotal = 0
    for item in order_list:
        subtotal += item['price']
    return subtotal    
 
 
def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    tax_rate = 0.15
    tax = round(subtotal * tax_rate,2)
    return tax    
    

def summarize_order(order_list):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total
    """
    print('Summarizing order...')
    names = [item['name']for item in order_list]
    subtotal = calculate_subtotal(order_list)
    tax = calculate_tax(subtotal)
    total = round(subtotal+tax,2)
    return names, total

def Final():
    show_menu()
    order = choose_item()
    names,total = summarize_order(order)
    
    print("\n Your Order Summary")
    for name in names:
        print(f"Item: {name}")
    print(f"Price: ${total}")
  

if True:    
    Final()     
    
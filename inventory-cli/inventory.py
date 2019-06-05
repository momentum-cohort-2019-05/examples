def get_second_item(seq):
    """
    Given a sequence of items, return the second element in
    that sequence.
    """
    return seq[1]


def print_quantities(quantities):
    """
    Given a dictionary of item codes and quantities, print 
    out those item codes and their quantities, sorted by
    the quantity of each item.
    """
    print("\n\nQuantities\n===========")
    quantities = sorted(quantities.items(), key=get_second_item)
    for item, qty in quantities:
        print(item, qty)


def enter_items(item_quantities):
    """
    Given a dictionary of item quantities,
    ask the user repeatedly to enter item codes.
    If the item already exists in the dictionary, add
    1 to its quantity; otherwise, add it to the dictionary
    with a quantity of 1.
    """
    while True:
        item = input("Enter code: ")
        if item == "":
            return

        if item in item_quantities:
            item_quantities[item] += 1
        else:
            item_quantities[item] = 1


def save_inventory(quantities):
    with open("inventory.txt", mode="w") as file:
        for code, qty in quantities.items():
            file.write(f"{code} {qty}\n")


def load_inventory(quantities):
    with open("inventory.txt", mode="r") as file:
        for line in file.readlines():
            line = line.strip()
            code, qty = line.split()
            quantities[code] = int(qty)


if __name__ == "__main__":
    item_quantities = {}
    load_inventory(item_quantities)

    while True:
        print("""
    Welcome to the ACME inventory system!

    1) Enter items
    2) Print quantities
    X) Exit
        """)
        option = input("Choose an option: ")

        if option == "1":
            enter_items(item_quantities)
        elif option == "2":
            print_quantities(item_quantities)
        elif option.lower() == "x":
            save_inventory(item_quantities)
            break

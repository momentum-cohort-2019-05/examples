# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

cover_price = 24.95
bookstore_discount = 0.4
shipping_first_copy = 3
shipping_additional_copies = 0.75

num_copies_as_str = input("How many copies are you ordering? ")
num_copies = int(num_copies_as_str)
cost_of_books = (cover_price * num_copies) * (1.0 - bookstore_discount)
cost_of_shipping = shipping_first_copy + (shipping_additional_copies *
                                          (num_copies - 1))

print("Your total cost is", round(cost_of_books + cost_of_shipping, 2))

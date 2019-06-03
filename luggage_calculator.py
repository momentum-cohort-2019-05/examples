# Description
# Ask the user for the weight of the current bag.
#   - If the user has no more bags, stop
#   - Otherwise, ask again
# Add up the weight of all bags
# If > limit (100 lbs), warn the user

done = False
total_weight = 0
weight_limit = 100

while not done:
    bag_weight_as_str = input(
        "How much does your bag weigh in pounds? (Hit Enter if you are done) ")
    if bag_weight_as_str == "":
        done = True
    else:
        bag_weight = int(bag_weight_as_str)

        # Equivalent: total_weight += bag_weight
        total_weight = total_weight + bag_weight
        print("Your total weight so far is " + str(total_weight) + ".")

if total_weight > weight_limit:
    print("Warning! You are over the weight limit by " +
          str(total_weight - weight_limit) + " pounds.")

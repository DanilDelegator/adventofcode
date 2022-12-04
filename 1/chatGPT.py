def solve_problem(calories):
    # initialize the maximum number of Calories to 0
    max_calories = 0

    # initialize the Elf carrying the maximum number of Calories to 0
    max_elf = 0

    # initialize the current Elf to 1
    elf = 1

    # loop through the calories
    for c in calories:
        # if the current item is a blank line, increment the Elf number
        if c == "":
            elf += 1
        else:
            # add the number of Calories to the current Elf's total
            elf_calories[elf] += int(c)

            # if the current Elf's total is greater than the maximum,
            # update the maximum and the Elf carrying the maximum
            if elf_calories[elf] > max_calories:
                max_calories = elf_calories[elf]
                max_elf = elf

    # return the Elf carrying the maximum number of Calories and their total
    return (max_elf, max_calories)

# read the input values from the provided string
input_values = "22243\n11899\n\n1696\n2595\n5331\n6092\n5274\n5641\n1345\n6626\n2005\n6260\n6410\n2092\n3501\n\n3982\n4505\n5836\n6059\n6513\n1151\n\n7002\n6597\n7174\n3618\n4734\n5107\n1388\n6493\n6541\n6440\n5291\n4492"

# split the input string into a list of strings
input_values = input_values.split("\n")

# initialize the dictionary containing the number of Calories carried by each Elf
# to 0 for all Elves
elf_calories = {}
for i in range(1, len(input_values)):
    elf_calories[i] = 0

# solve the problem using the input values
result = solve_problem(input_values)

# print the result
print("Elf %d is carrying the most Calories: %d" % (result[0], result[1]))
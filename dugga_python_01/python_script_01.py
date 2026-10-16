###

## Q1

# a)

# own name saved as a string in a variable

my_name = "Dan Kolnik"

# b)

# calculate and print the length of own name

print(len(my_name))

# c)

# chose a letter "n", which occurs in own name at least once

# created counter to count a specific letter
n_count = 0

# created for loop to list through letters in a string
# and increase counter when it sees letter "n"
for letter in my_name:
    if letter == "n":
        n_count += 1
print(n_count)

###################################################################

## Q2

# use the following list for solving this question

my_list = [1, 5, "4", "six", 3.14]


# a)

# created new list to add numbers into
new_list = []

# made a for loop to chande strings into integers and
# add all numbers to a new_list
for thing in my_list:
    if type(thing) != int:
        if type(thing) == float:
            # here I would like to convet float to integer
            round(thing, 0)
        #if type(thing) == str:
            # here I would want to convert string to integer
    if type(thing) == int:
        new_list.append(thing)
    else:
        # this is meant for strings like "six", which I am not aware how to convert to integer
        print(f"{thing} could not be converted to an integer and wasn't added to the new_list")

print(new_list)


# b)

# I have put the conversion loop in a function called clean_list(),
# which returns new_list

def clean_list(my_list):
    for thing in my_list:
        if type(thing) != int:
            if type(thing) == float:
                # here I would like to convet float to integer
                round(thing, 0)
            #if type(thing) == str:
                # here I would want to convert string to integer
        if type(thing) == int:
            new_list.append(thing)
        else:
            # this is meant for strings like "six", which I am not aware how to convert to integer
            print(f"{thing} could not be converted to an integer and wasn't added to the new_list")
    return new_list

#
print(new_list)


# c)

# I did not manage to make a well functional loop in 2 a),
# so I will define a new list
new_list_02 = [1, 5, 4, 3]

# create a list where I will add sum of adjacent numbers
sum_adj_numbers = []

# adding counter so the loop will count only sum of two adjacent numbers
rounding_2_sum = 0

# summing adjacent integers in loop
sum_adj = 0

# I tried to create a loop that would reset variables so it will sum
# only adjacent values and then reset variables to zero to count only
# adjacent values again
for number in new_list_02:
    if rounding_2_sum == 0:
        rounding_2_sum += 1
        sum_adj += number
    if rounding_2_sum == 1:
        rounding_2_sum += 1
        sum_adj += number
        sum_adj_numbers.append(sum_adj)
    if rounding_2_sum == 2:
        rounding_2_sum = 1
        sum_adj = 0
        sum_adj += number

print(sum_adj_numbers)

###################################################################

## Q3


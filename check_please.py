import math

## Import Math to for ceil function, rounds to nearest whole number

def split_check(total, number_of_people): 
    return math.ceil(total / number_of_people)

total_due = float(input("What is the total?  "))
number_of_people = int(input("How many people are there?   "))

amount_due = split_check(total_due, number_of_people)


print("Each person owes ${}" .format(amount_due))
                         
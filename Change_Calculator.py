import math
from pprint import pprint

coins = {
    "quarter": 25,
    "dime": 10,
    "nickel": 5,
    "penny":1
}

cost = float(input("Enter a cost: $"))

while True:
    try:
        money_given = float(input("Enter the amount of money given: $"))
    except:
        # not given a float or integer
        print(f"Enter an integer or float\n")
    else:
        if money_given < cost:
            print("Please provide more money to calculate change.\n")
        else:
            break

# money_given = int(money_given*100)
# cost = int(cost*100)

# Calculate the difference
difference = money_given-cost

# Separate the dollar bills from the change to be calculated
change, bills = math.modf(difference)
change = round(change, 2)

if change == 0 and bills == 0:
    print("You gave exact change. Nothing to return.")

else:
    print(f"Your change is ${round(difference,2)}")
    # Work with change as an integer
    change = int(change*100)

    change_in_coins = {}

    for currency in coins:
        quotient,remainder = divmod(change,coins[currency])
        change_in_coins[currency] = quotient # number of coins
        change = remainder

    print(f"${bills} in bills\n{change_in_coins['quarter']} quarters\n{change_in_coins['dime']} dimes"
          f"\n{change_in_coins['nickel']} nickels\nand {change_in_coins['penny']} pennies")
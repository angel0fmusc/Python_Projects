"""
Change Calculator
Given the cost of an item and the amount given, calculate the change to return to the user
and the number of specific coins (quarter, dime, nickel, and penny) to return.
"""

import math


class ChangeCalc:
    def __init__(self):
        self.change_in_coins = {}
        self.cost = 0
        self.money_given = 0
        self.change = None
        self.bills = None

    def get_cost(self):
        """
        Ask user for input and confirm if user inputs an integer or float.
        Otherwise, continue to ask for input
        :return: None
        """
        while True:
            try:
                self.cost += float(input("Enter a cost: $"))
                break
            except ValueError:
                print("That was not a valid number. Try again...")

    def money_for_item(self):
        """
        Ask user for input of either integer or float.
        If correct input received, but amount is less than the cost, add the amount until both the cost
        and money given are equal.
        :return: None
        """
        while True:
            try:
                self.money_given += float(input("Enter the amount of money given: $"))
                if self.money_given < self.cost:
                    print("Please provide more money to calculate change.\n"
                          f"Current cost of item: ${self.cost}\n"
                          f"Current amount given: ${round(self.money_given,2)}\n")
                else:
                    break
            except ValueError:
                print("That was not a valid number. Try again...")

    def difference_in_cost(self):
        """
        Calculate the difference in the cost and amount given
        :return: None
        """
        difference = self.money_given - self.cost
        print(f"Your change is ${round(difference, 2)}")

        # Separate the bills from the change
        self.change, self.bills = math.modf(difference)

        # Round the current change to 2 decimal points
        self.change = round(self.change, 2)
        self.coins_for_change()

    def coins_for_change(self):
        """
        Determine the number of coins needed to give back change.
        Print the number of coins that are being returned as change
        :return: None
        """
        if self.bills == 0 and self.change == 0:
            print("You gave exact change. Nothing to return.")
        else:
            coins = {
                "quarter": 25,
                "dime": 10,
                "nickel": 5,
                "penny": 1
            }
            # Work with the change as an int
            change = int(self.change*100)

            # Loop through dictionary of coin values and divide into change to return
            for currency in coins:
                quotient, remainder = divmod(change, coins[currency])
                self.change_in_coins[currency] = quotient    # Add number of coins to new dictionary
                change = remainder                      # Remaining coins to calculate change

            print(f"${self.bills} in bills")
            for num_change in self.change_in_coins:
                if self.change_in_coins[num_change] != 0:
                    if self.change_in_coins[num_change] == 1:
                        print(f"{self.change_in_coins[num_change]} {num_change}")
                    elif self.change_in_coins[num_change] > 1 and num_change == "penny":
                        print(f"{self.change_in_coins[num_change]} pennies")
                    else:
                        print(f"{self.change_in_coins[num_change]} {num_change}s")


my_change = ChangeCalc()
my_change.get_cost()
my_change.money_for_item()
my_change.difference_in_cost()

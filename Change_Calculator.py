"""
Change Calculator
Given the cost of an item and the amount given, calculate the change to return to the user
and the number of specific coins (quarter, dime, nickel, and penny) to return.
"""

import math


class ChangeCalc:
    def __init__(self):
        self.complete_change = {}
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
        if self.bills == 0 and self.change == 0:
            print("You gave exact change. Nothing to return.")
        else:
            self.bills_coins_change("bills")
            self.bills_coins_change("coins")
            self.print_money()

    def bills_coins_change(self, flag):
        """
        Determine the least amount of change to give back in bills and coins.
        Flag will determine what dictionary to create and how the change will be divided
        :param flag: string, either 'bills' or 'coins'
        :return: None
        """
        if flag == "bills":
            # If there is no dollars to return, exit the function
            if self.bills == 0:
                print("No bills to return")
                return
            # Otherwise, create a dictionary and variable for bills as ints
            else:
                change = {
                    "one-hundred": 100,
                    "fifty": 50,
                    "twenty": 20,
                    "ten": 10,
                    "five": 5,
                    "one": 1
                }
                money = int(self.bills)
                # print(f"${self.bills} in bills")

        # flag is coins
        else:
            # If there is no coins, exit the function
            if self.change == 0:
                print("No coins to return")
                return
            else:
                change = {
                    "quarter": 25,
                    "dime": 10,
                    "nickel": 5,
                    "penny": 1
                }
                money = int(self.change*100)
                # print(f"${self.change} in coins")

        # Loop through dictionary and device into change to return
        for currency in change:
            quotient, remainder = divmod(money, change[currency])
            self.complete_change[currency] = quotient   # Add the number of bills/coins to the instance dictionary
            money = remainder

# TO-DO: Need to adjust for all dict keys that end in 'y'
    def print_money(self):
        """
        Print the change in the instance dictionary
        :return: None
        """
        for money in self.complete_change:
            if self.complete_change[money] != 0:
                if self.complete_change[money] == 1:
                    print(f"{self.complete_change[money]} {money}")
                elif self.complete_change[money] > 1 and money == "penny":
                    print(f"{self.complete_change[money]} pennies")
                else:
                    print(f"{self.complete_change[money]} {money}s")


my_change = ChangeCalc()
my_change.get_cost()
my_change.money_for_item()
my_change.difference_in_cost()

'''
Blackjack game
'''

import random

# Global variables
suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        '''
        Constructor
        Start with an empty list
        Loop through the suits tuple, loop through the ranks tuple, and create a Card object from each suit and rank
        Append the Card object to the list
        '''
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return f'This deck has: {deck_comp}'

    def shuffle(self):
        '''
        Shuffle the list of Card objects using random library shuffle() method
        :return: Nothing, list shuffles in place
        '''
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


class Hand:

    def __init__(self):
        self.cards = []     # Empty hand
        self.value = 0      # Sum of hand
        self.aces = 0       # Number of Aces

    def __str__(self):
        hand_comp = ''
        for card in self.cards:
            hand_comp += '\n' + card.__str__()
        return f'Hand consists of: {hand_comp}\nValue: {self.value}'

    def add_card(self, card):
        '''
        Add card to current hand
        :param card: object consisting of rank and suit
        :return:
        '''
        self.cards.append(card)

        # Get the value of the card by the rank and add to current value
        self.value += values.get(card.rank)

        # Increment the number of Aces in hand if card is an Ace
        if card.rank == 'Ace':
            self.aces += 1

        # Check if value needs to be adjusted
        self.ace_adjust()

    def ace_adjust(self):
        '''
        If hand consist of Aces, need to determine if more valuable for value of 1 or 11
        :return:
        '''
        if self.value > 21 and self.aces != 0:
            self.value -= 10        # Subtract 10 from the value
            self.aces -= 1          # Subtract the number of aces to account for adjustment

    def value_check(self):
        print(f"Current value: {self.value}")

deck = Deck()

deck.shuffle()

hand = Hand()

while hand.value <= 21:
    hand.add_card(deck.deal())
    print(hand)


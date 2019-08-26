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
        """
        Constructor
        Start with an empty list
        Loop through the suits tuple, loop through the ranks tuple, and create a Card object from each suit and rank
        Append the Card object to the list
        """
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
        """
        Shuffle the list of Card objects using random library shuffle() method
        :return: Nothing, list shuffles in place
        """
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
        return hand_comp

    def add_card(self, card):
        """
        Add card to current hand
        :param card: object consisting of rank and suit
        :return:
        """
        self.cards.append(card)

        # Get the value of the card by the rank and add to current value
        self.value += values[card.rank]

        # Increment the number of Aces in hand if card is an Ace
        if card.rank == 'Ace':
            self.aces += 1

    def ace_adjust(self):
        """
        If hand consist of Aces, need to determine if more valuable for value of 1 or 11
        :return:
        """
        if self.value > 21 and self.aces != 0:
            self.value -= 10        # Subtract 10 from the value
            self.aces -= 1          # Subtract the number of aces to account for adjustment


class Player:

    def __init__(self):
        self.hand = Hand()
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet * 2

    def lose_bet(self):
        self.total -= self.bet

    def place_bet(self):
        """
        Ask player for bet.
        Player's bet must be a number and cannot exceed number of chips.
        :return: None
        """

        while True:
            try:
                self.bet = int(input("Place your bet: "))
            except ValueError:
                print("You did not enter a number.")
            else:
                if self.bet > self.total:
                    print(f"Your bet cannot exceed {self.total}.")
                else:
                    break

    def hit(self, deck):
        """
        Player requests another card from the dealer.
        Check if the value of the hand needs to be adjusted due to an Ace
        :param deck: instance of a Deck containing Card objects
        :return: None
        """
        self.hand.add_card(deck.deal())

        # Check if value needs to be adjusted
        self.hand.ace_adjust()


def hit_or_stay(deck, player):
    """
    Current player determines to hit or stay
    :param deck: Deck object of Card objects
    :param player: Player object
    :return: None
    """
    global playing

    while True:
        choice = input("Would you like to hit or stay? Enter h or s: ")
        # Player chooses to hit
        if choice[0].lower() == 'h':
            player.hit(deck)
        # Player chooses to stay
        elif choice[0].lower() == 's':
            print("Player stays. Dealer's turn.")
            playing = False
        # Player did not choose either
        else:
            print("Please choose again.")
            continue
        break


def show_hands_some(dealer, player):
    '''
    Dealer should have 2 cards. This fuction only shows one of the
    Dealer's cards and all of the Player's cards.
    :param dealer: has a hand of Card objects
    :param player:
    :return:
    '''
    # Show the dealer's first card
    print(f"Dealer:\n{dealer.hand.cards[0]}")

    # Show all of player's hand
    print(f"Player:{player.hand}")


def show_hands_all(dealer, player):
    """
    Dealer and player each show all cards
    :param dealer: has a Hand of Card objects
    :param player:
    :return:
    """
    # Show dealer's hand and value
    print(f"Dealer:{dealer.hand}\nValue: {dealer.hand.value}")

    # Show player's hand and value
    print(f"Player:{player.hand}\nValue: {player.hand.value}")


def player_wins(player):
    """
    Player wins in one of 3 ways:
        - Hand gets 21 points on first two cards (blackjack) without dealer blackjack
        - Final score higher than dealer without exceeding 21
        - Dealer busts
    :param player: Object, had a hand of Card objects
    :return:
    """
    return player.hand.value == 21 or player.hand.value < 21


def player_busts(player):
    """
    Player hand > 21
    :return: Boolean
    """
    return player.hand.value > 21


# Gameplay
if __name__ == "__main__":

    # Create a deck of cards and shuffle
    deck = Deck()
    deck.shuffle()

    # Create players
    player1 = Player()
    dealer = Player()

    # Have player place bet
    player1.place_bet()

    # Deal 2 cards each to dealer and player
    dealer.hit(deck)
    dealer.hit(deck)
    player1.hit(deck)
    player1.hit(deck)

    # Show initial hand
    show_hands_some(dealer, player1)

    while playing:
        pass

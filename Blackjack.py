'''
Blackjack game
'''

import random

# Global variables
suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}
playing = True


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
        Loop through the suits tuple, loop through the ranks tuple, and
        create a Card object from each suit and rank
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
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []     # Empty hand
        self.value = 0      # Sum of hand
        self.aces = 0       # Number of Aces

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


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace_adjust()


def hit_or_stay(deck, hand):
    """
    Current player determines to hit or stay
    :param deck: Deck object of Card objects
    :param player: Player object
    :return: None
    """
    global playing   # to control while loop in scope

    while True:
        choice = input("Would you like to hit or stay? Enter h or s: ")
        # Player chooses to hit
        if choice[0].lower() == 'h':
            hit(deck, hand)
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
    """
    Dealer should have 2 cards. This fuction only shows one of the
    Dealer's cards and all of the Player's cards.
    :param dealer: has a hand of Card objects
    :param player:
    :return:
    """
    # Show the dealer's first card
    print(f"\nDealer:")
    print("<card hidden>")
    print('', dealer.cards[1])
    print(f"\nPlayer:",*player.cards, sep='\n ')


def show_hands_all(dealer, player):
    """
    Dealer and player each show all cards
    :param dealer: has a Hand of Card objects
    :param player:
    :return:
    """
    print("\nDealer:", *dealer.cards, sep='\n ')
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer:", *player.cards, sep='\n ')
    print("Player's Hand = ", player.value)


def player_wins(player,dealer,chips):
    """
    Player wins in one of 3 ways:
        - Hand gets 21 points on first two cards (blackjack) without dealer blackjack
        - Final score higher than dealer without exceeding 21
        - Dealer busts
    :param chips:
    :param dealer:
    :param player: Object, had a hand of Card objects
    :return:
    """
    print("PLAYER WINS!!")
    chips.win_bet()


def player_busts(player,dealer,chips):
    """
    Player hand > 21
    :return: Boolean
    """
    print("BUST PLAYER")
    chips.lose_bet()


def dealer_wins(player,dealer,chips):
    """
    Dealer wins if:
    - hand == 21
    - greater than player's hand, but less than 21
    :param dealer:
    :return:
    """
    print("DEALER WINS!")
    chips.lose_bet()


def dealer_busts(player,dealer,chips):
    """
    Dealer busts if hand exceeds 21
    :param dealer: object with Hand of Card objects
    :return: Boolean
    """
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()


def push(player,dealer):
    print('Dealer and player tie! PUSH')


# Gameplay
if __name__ == "__main__":

    while True:
        print("Welcome to Blackjack")

        # Create a deck of cards and shuffle
        deck = Deck()
        deck.shuffle()

        # Player - add 2 cards from deck
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        # Dealer - add 2 cards from deck
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Player's chips
        player_chips = Chips()

        # Prompt player for bet
        take_bet(player_chips)

        # Show cards (keep one dealer card hidden)
        show_hands_some(dealer_hand, player_hand)

        while playing:
            hit_or_stay(deck,player_hand)

            # Show cards
            show_hands_some(dealer_hand, player_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

            show_hands_all(dealer_hand, player_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)

        print('\n Player total chips are at: {}'.format(player_chips.total))

        new_game = input("Would you like to play another hand? y/n")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thank you for playing!")
            break

# Poker Hand Game

import random

# Deck class
class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]

# Function to deal initial hand
def deal_initial_hand(deck):
    return [deck.deal() for _ in range(5)]

# Function to replace cards in hand
def replace_cards(deck, hand, indices):
    for index in indices:
        hand[index - 1] = deck.deal()
    return hand

# Function to get user input
def get_user_input():
    indices = input("Enter the positions (1-5) of the cards you want to replace, separated by commas: ")
    indices = indices.split(',')
    return [int(index.strip()) for index in indices]

# Main game function
def main():
    deck = Deck(52)
    hand = deal_initial_hand(deck)

    print("\nYour initial hand:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")

    indices = get_user_input()

    hand = replace_cards(deck, hand, indices)

    print("\nYour final hand:")
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")

if __name__ == "__main__":
    main()

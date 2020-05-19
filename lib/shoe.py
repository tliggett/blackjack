from enum import Enum
import random


class Suit(Enum):
    heart = 1
    spade = 2
    club = 3
    diamond = 4

class Rank(Enum):
    ace = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return f'{self.suit} {self.rank}'


class Shoe:
    def __init__(self, deck_count: int):
        self.cards = self.__get_cards(deck_count)
        self.deck_count = deck_count
        self.discard_shown = []
        self.discard_hidden = []

    def deal(self):
        card = self.cards.pop(0)
        self.discard_shown.append(card)
        return card

    def burn(self):
        card = self.cards.pop(0)
        self.discard_hidden = card

    def shuffle(self):
        random.shuffle(self.cards)

    def cards_left(self):
        return len(self.cards)


    def __get_cards(self, deck_count):
        cards = []
        for i in range(deck_count):
            for suit in Suit:
                for rank in Rank:
                    cards.append(Card(suit, rank))
        return cards

    def __str__(self):
        s = ""
        s += f'cards left: {self.cards_left()   }'
        # for card in self.cards:
           #  s += f'{card}'
        return s

if __name__ == "__main__":

    ace_hearts = Card(suit=Suit.heart, rank=Rank.ace)
    print(f'This is the card: {ace_hearts}')

    shoe = Shoe(2)
    shoe.shuffle()
    print(f'{shoe}')
    shoe.burn()
    print(f'{shoe.deal()}')
    print(f'{shoe.deal()}')
    print(f'{shoe.deal()}')
    print(f'{shoe.deal()}')
    print(f'{shoe}')

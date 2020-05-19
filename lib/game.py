from shoe import Shoe, Card, Rank, Suit


class BlackJackTable:
    def __init__(self, hands: int, players):
        self.hands_to_play = hands
        self.hands_played = 0
        self.players = players # write player implementation
        self.shoe = Shoe(6) # write card shoe implementation  




class Player:
    def __init__(self):
        self.hand = []

    def hand_value(self):
        value = 0
        for card in self.hand:
            value += self.__card_value(card)

        if value > 21:
            value = 0
            for card in self.hand:
                value += self.__card_value(card, aces_high=False)

        return value

    def __card_value(self, card: Card, aces_high=True):
        if card.get_rank() == Rank.ace:
            if aces_high:
                return 11
            else:
                return 1
        elif card.get_rank() == Rank.two:
            return 2
        elif card.get_rank() == Rank.three:
            return 3
        elif card.get_rank() == Rank.four:
            return 4
        elif card.get_rank() == Rank.five:
            return 5
        elif card.get_rank() == Rank.six:
            return 6
        elif card.get_rank() == Rank.seven:
            return 7
        elif card.get_rank() == Rank.eight:
            return 8
        elif card.get_rank() == Rank.nine:
            return 9
        elif card.get_rank() == Rank.ten or card.get_rank() == Rank.jack:
            return 10
        elif card.get_rank() == Rank.queen or card.get_rank() == Rank.king:
            return 10
        else:
            return -999



if __name__ == "__main__":
    izzy = Player()
    shoe = Shoe(6)
    shoe.shuffle()
    shoe.burn()
    izzy.hand.append(shoe.deal())
    izzy.hand.append(shoe.deal())
    while izzy.hand_value() < 17:
        print(f'{izzy.hand_value()}')
        izzy.hand.append(shoe.deal())

    print(f'Final Hand Value: {izzy.hand_value()}')
    

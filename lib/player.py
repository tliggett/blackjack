import json

from lib.shoe import Shoe, Card, Rank, Suit



class Player:
    def __init__(self, payroll=500):
        self.hand = []
        self.type = 'human'
        self.payroll = payroll
        self.wager = 0
        with open('lib/human.json') as f:
            self.moves = json.load(f)

    def hand_value(self, hand=None):
        if hand is None:
            hand = self.hand
        hand = sorted(hand)
        value = 0
        first_ace = True
        for card in hand:
            if first_ace:
                value += card.value()
                if card.value() == 11:
                    first_ace = False
            else:
               value += card.value(aces_high=False) 
            
        if value > 21:
            value = 0
            for card in hand:
                value += card.value(aces_high=False)

        return value

    def bet(self, minimum=10):
        self.payroll = self.payroll - minimum
        self.wager = minimum
        return minimum 

    def play(self, shoe: Shoe, dealer_card: Card):
        move = ""
        if self.hand_value() > 21:
            move = "BUST"
        elif self.hand_value() == 21:
            if len(self.hand) == 2:
                move = "BLACKJACK"
            else:
                move = "S"
        else:
             move = self.moves["hand"][self.hand_str()][dealer_card.char_rep()]
        # print(f'{self.hand_value()} : {move}')
        return move

    def pay(self, payout):
        self.payroll = self.payroll + payout
        self.wager = 0

    def hand_str(self):
        hand_s = sorted(self.hand)
        handstr = ""
        for card in hand_s:
            handstr += card.char_rep()
        if len(self.hand) > 2:
            if "A" not in handstr:
                handstr = f'H{self.hand_value()}'
            elif self.__hand_is_soft():
                handstr = f'S{self.hand_value()}'
            else:
                handstr = f'H{self.hand_value()}'
        return handstr

    def __hand_is_soft(self):
        hard_value = self.__get_aces() + self.hand_value(self.__pull_aces())
        # print(self.hand)
        if hard_value <= 11:
            return True
        return False 

    def __pull_aces(self, hand=None):
        if hand is None:
            hand = self.hand
        no_aces = []
        for card in hand:
            if card.get_rank() is not Rank.ace:
                no_aces.append(card)
        return no_aces


    def __get_aces(self):
        hand_s = sorted(self.hand)
        ace_count = 0
        for card in hand_s:
            if card.get_rank() == Rank.ace:
                ace_count = ace_count + 1
        return ace_count

if __name__ == "__main__":
    izzy = Player()
    shoe = Shoe(6)
    shoe.shuffle()
    shoe.burn()
    dealer_card = shoe.deal()
    print(f'Dealer card: {dealer_card}')
    izzy.hand.append(shoe.deal())
    izzy.hand.append(shoe.deal())
    print(f'{izzy.hand_str()}')
    while izzy.play(shoe, dealer_card) == "H":
       izzy.hand.append(shoe.deal())
       print(f'{izzy.hand_str()}')

    print(f'Final Hand Value: {izzy.hand_value()}')
    

import random

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    
    def __init__(self):
        self.cards = []
    
        # List of suit categories
        self.suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        
        # suit rank 
        self.ranks = [
            { "rank": "A" , "value": 11  },
            { "rank": "2" , "value": 2  },
            { "rank": "3" , "value": 3  },
            { "rank": "4" , "value": 4  },
            { "rank": "5" , "value": 5  },
            { "rank": "6" , "value": 6  },
            { "rank": "7" , "value": 7  },
            { "rank": "8" , "value": 8  },
            { "rank": "9" , "value": 9  },
            { "rank": "10" , "value": 10  },
            { "rank": "J" , "value": 10 },
            { "rank": "Q" , "value": 10  },
            { "rank": "K" , "value": 10  },
        ]
        self.cardFiller()

    def cardFiller(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards) if len(self.cards) > 1 else self.cards

    def deal(self, numer):
        card_dealt = []
        for i in range(numer):
            if len(self.cards) > 0 : card_dealt.append(self.cards.pop())
        return card_dealt
    
class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer    
    
    def addCard(self, card_list):
        self.cards.extend(card_list)

    def calculateValue(self):
        self.value = 0
        hasAce = False
        for card in self.cards:
            cardValue = int(card.rank["value"])
            self.value += cardValue
            if card.rank["rank"] == "A":
                hasAce = True
        if hasAce and self.value > 21:
            self.value -= 10
        # return self.value
    
    def getValue(self):
        self.calculateValue()
        return self.value

    def isBlackJack(self):
        return self.getValue() == 21
    
    def display(self):
        print(f'''{"Dealer's" if  self.dealer else "Your's"} hand:''')

        for card in self.cards:
            print(card)
        
        if not self.dealer:
            print("Value:", self.getValue())
        print()


deck = Deck()
deck.shuffle()

hand = Hand()
hand.addCard(deck.deal(2))
hand.display()
import random

# List of suit categories
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

# suit rank 
ranks = [
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

# list of 52 cards
cards = []

def cardFiller():
    for suit in suits:
        for rank in ranks:
            cards.append([suit, rank])

def shuffle():
    random.shuffle(cards)

def deal(numer):
    card_dealt = []
    for i in range(numer):
        card_dealt.append(cards.pop())
    return card_dealt

def main():
    cardFiller()
    shuffle()
    card = deal(1)[0]
    print(card[1]['value'])

if __name__ == "__main__":
    main()
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
    
    def display(self, show_all_dealet_cards=False):
        print(f'''{"Dealer's" if  self.dealer else "Your's"} hand:''')

        for i, card in enumerate(self.cards):
                print("Hidden") if i == 0 and self.dealer and not show_all_dealet_cards and not self.isBlackJack() else print(card)
        
        if not self.dealer:
            print("Value:", self.getValue())
        print()


class Game:

    def checkWinner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.getValue() > 21:
                print("You busted!! Dealer win...")
                return True
            elif dealer_hand.getValue() > 21:
                print("Dealer busted!! You win...")
                return True
            elif dealer_hand.isBlackJack() and player_hand.isBlackJack():
                print("Both have a BlackJack. it's a Tie")
            elif player_hand.isBlackJack():
                print("You have a BlackJack. You win...")
                return True
            elif dealer_hand.isBlackJack():
                print("Dealer have a BlackJack. Dealer win...")
                return True
        else:
            if player_hand.getValue() > dealer_hand.getValue():
                print("You win...")
            elif player_hand.getValue() == dealer_hand.getValue():
                print("It's a Tie")
            else:
                print("Dealer win...")
            return True
        return False
    
    def Play(self):
        self.game_number = 0
        self.games_to_play = 0

        while self.games_to_play <= 0:
            try:
                self.games_to_play = int(input("How many games do you want to play? "))
            except Exception as e:
                print("You must enter a number.") if not isinstance(self.games_to_play , int) else print(e)

        while self.game_number < self.games_to_play:
            self.game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.addCard(deck.deal(1))
                dealer_hand.addCard(deck.deal(1))
            print()
            print("*"*30)
            print(f"Game {self.game_number} of  {self.games_to_play}")
            print("*"*30)

            player_hand.display()
            dealer_hand.display()

            if self.checkWinner(player_hand, dealer_hand):
                continue
            choice = ""
            while choice not in ["hit", "stand"] and choice not in ["s", "stand"]:
                choice = input("Do you want to hit or stand? ").lower()
                print()
                while choice not in ["hit", "h", "s", "stand"]:
                    choice = input("Please choose Hit/Stand or H/S: ").lower()
                    print()
                
                if choice in ["hit", "h"]:
                    player_hand.addCard(deck.deal(1))
                    player_hand.display()
                    print()
            if self.checkWinner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.getValue()
            dealer_hand_value = dealer_hand.getValue()

            while dealer_hand_value < 17:
                dealer_hand.addCard(deck.deal(1))
                dealer_hand_value = dealer_hand.getValue()
            dealer_hand.display(show_all_dealet_cards=True)

            if self.checkWinner(player_hand, dealer_hand):
                continue
                
            print("Final Results")
            print(f"Player Hand Value: {player_hand_value}")
            print(f"Dealer Hand Value: {dealer_hand_value}")

            self.checkWinner(player_hand, dealer_hand, True)
        
        print(" \n Thanks for Play!!")




g = Game()
g.Play()
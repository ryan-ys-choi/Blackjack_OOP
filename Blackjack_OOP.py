import random

suits = ["♥ hearts", "♦ diamonds", "♣ clubs", "♠ spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def value(self):
        if self.rank in ["jack", "queen", "king"]:
            return 10
        elif self.rank == "ace":
            return 11
        else:
            return int(self.rank)
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

class Hand: 
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.hand.append(card)
        self.value += card.value()
        if card.rank == "ace":
            self.aces += 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    
    def show_cards(self):
        for card in self.hand:
            print(card)
        print()

class BlackjackGame:
    def __init__(self):
        self.is_game_over = False
    def play_game(self):
        while not self.is_game_over:
            print("\nLet's play Blackjack \n")
            deck = Deck()

            # Deal two cards to player and dealer
            player_hand = Hand()
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())

            dealer_hand = Hand()
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())

            # Print the player's and dealer's cards
            print("Player's cards: ")
            player_hand.show_cards()
            print("Dealer's cards: ")
            dealer_hand.show_cards()

            # If player wants to double down
            if player_hand.value in [9, 10, 11]:
                user_choice = input("Double down? (Yes/No) ")
                if user_choice.lower() == "yes":
                    additional_card = deck.deal()
                    player_hand.add_card(additional_card)
                    print("Additional card for the player: ")
                    print(additional_card)
                else:
                    if player_hand.value < 21:
                        user_choice = input("Hit or Stand? ")
                        if user_choice.lower() == "hit":
                            player_new_card = deck.deal()
                            player_hand.add_card(player_new_card)
                            print("\nNew card for the player: ")
                            print(player_new_card)
                        else:
                            break
            
            while player_hand.value < 21:
                    user_choice = input("Hit or Stand? ")
                    if user_choice.lower() == "hit":
                        player_new_card = deck.deal()
                        player_hand.add_card(player_new_card)
                        print("\nNew card for the player: ")
                        print(player_new_card)
                    else:
                        break
            
            # dealer keeps hitting until it reaches 17
            while dealer_hand.value < 17:
                dealer_new_card = deck.deal()
                dealer_hand.add_card(dealer_new_card)
                print("\nNew card for the dealer: ")
                print(dealer_new_card)            
            
            if 16 < player_hand.value < 21 and 16 < dealer_hand.value < 21 and player_hand.value == dealer_hand.value:
                print("\nPush\n")

            elif player_hand.value > 21:
                print("\nYou lose, it went over 21\n")

            elif dealer_hand.value > 21:
                print("\nYou win, Dealer went over 21\n")

            elif player_hand.value > dealer_hand.value:
                print("\nYou win\n")

            elif dealer_hand.value > player_hand.value:
                print("\nYou lose\n")
            
            print(f"Player's total score: {player_hand.value}")
            print(f"Dealer's total score: {dealer_hand.value}")

            self.is_game_over = True

game = BlackjackGame()
game.play_game()

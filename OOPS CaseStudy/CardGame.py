import random

# ------------------------------
# Card: holds rank + suit
# ------------------------------
class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2","3","4","5","6","7","8","9","10",
             "Jack","Queen","King","Ace"]

    rank_values = {rank: i for i, rank in enumerate(ranks, start=2)}

    def __init__(self, rank, suit):
    
        self.rank = rank
        self.suit = suit
        self.value = Card.rank_values[rank]


    def __str__(self):
        return f"{self.rank} of {self.suit}"


# ------------------------------
# Deck: generates and shuffles cards
# ------------------------------
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None
    
    def add_card(self, card):
        self.cards.append(card)


# ------------------------------
# Hand: holds cards of a player
# ------------------------------
class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def show(self):
        return [str(card) for card in self.cards]

    def highest_card(self):
        return max(self.cards, key=lambda c: c.value) if self.cards else None


# ------------------------------
# Player
# ------------------------------
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def show_hand(self):
        print(f"{self.name}'s hand:", self.hand.show())
        return self.hand.show()


# ------------------------------
# Card Game Engine
# ------------------------------
class CardGame:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.deck.shuffle()
        self.turn = 0

    def deal_cards(self, count):
        for _ in range(count):
            for player in self.players:
                card = self.deck.draw()
                if card:
                    player.hand.add(card)

    def play_turn(self):
        player = self.players[self.turn]
        card = self.deck.draw()

        if not card:
            print("Deck is empty!")
            return

        player.hand.add(card)
        print(f"{player.name} drew {card}")

        self.turn = (self.turn + 1) % len(self.players)

    # --------------------------
    # Decide winner by highest card
    # --------------------------
    def decide_winner(self):
        ranked = []
        for p in self.players:
            high = p.hand.highest_card()
            ranked.append((p, high))

        winner, high_card = max(ranked, key=lambda x: x[1].value)

        print(f"Winner is {winner.name} with highest card: {high_card}")
        return winner


# ------------------------------
# Usage
# ------------------------------
player1 = Player("Alice")
player2 = Player("Bob")

game = CardGame([player1, player2])

game.deal_cards(5)

player1.show_hand()
player2.show_hand()

game.decide_winner()

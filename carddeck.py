import random

from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        # make the deck
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return tuple(self._cards)

    def __len__(self):  # implement len()
        return len(self._cards)

    def __str__(self):  # implement str()
        my_class_name = type(self).__name__
        return f"{my_class_name}:{len(self)}"

    def __repr__(self):  # implement repr()
        my_class_name = type(self).__name__
        return f"{my_class_name}()"

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(d1)
    print(f"{d1 = }")
    
    d1.shuffle()
    print(f"{d1.cards = }")
    print(f"{len(d1) = }")
    for i in range(5):
        print(d1.draw())
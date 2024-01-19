from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call method in parent...
        for _ in range(2):
            card = Card("JOKER", "JOKER")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j)
    print(j.cards)
    for i in range(5):
        print(j.draw())
    
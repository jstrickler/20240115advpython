
class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank  # store data in object
        self._suit = suit
        # _spam is "private"

    @property # modifies rank()
    def rank(self):   #  getter property
        return self._rank

    @rank.setter
    def rank(self, value):  # setter property
        self._rank = value  

    @property
    def suit(self):
        return self._suit

    # human-friendly
    def __str__(self):
        return f"{self.rank}-{self.suit}"
    
    # Python-friendly
    def __repr__(self):
        # Card('4', 'Diamonds')
        return f"Card('{self.rank}', '{self.suit}')"


if __name__ == "__main__":
    c = Card('4', 'Diamonds')
    print(f"{c = }")
    print(f"{c.rank = }")
    print(f"{c.suit = }")
    c.rank = "8"
    print(f"{c.rank = }")
    print(c)

    
    
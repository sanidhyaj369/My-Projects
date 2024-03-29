class Card:
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]      #class variable
    rank_names = [None,'Ace','Two','Three', 'Four','Five','Six','Seven','Eight','Nine','Ten','Jack', 'Queen','King']
    
    def __init__(self, suit, rank):          #constructor
        pass

    def __str__(self):                      #for pretty printing
        pass

    def __cmp__(self, other):      #for compairing one card to another
        pass
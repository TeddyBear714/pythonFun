class Player:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        
    def set_cards(self,cards):
        self.cards = cards
        
    def set_seat(self,seat):
        self.seat = seat
        
    def set_money(self,money):
        self.money = money
        

p1 = Player("George",2000)

p1.set_money(1000)

print(p1.name)
print("\n")
print(p1.money)

class Card:
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit

class Table:
    def __init__(self,number_of_players):
        self.number_of_players = number_of_players
        self.deck1 = []
        for suit in ["spades","clubs","diamonds","hearts"]:
            for i in range(1,14):
                if i==1:
                    self.deck1.append(Card("Ace",suit))
                    continue
                if i==11:
                    self.deck1.append(Card("Jack",suit))
                    continue
                if i==12:
                    self.deck1.append(Card("Queen",suit))
                    continue
                if i==13:
                    self.deck1.append(Card("King",suit))
                    continue
                self.deck1.append(Card(str(i),suit))
        
                
t = Table(2)

for i in t.deck1:
    print([i.number,i.suit])

#print(t.deck1)
    #def shuffler(self):
            

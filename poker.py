import random


class Player:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.cards = "0"
        self.seat = "0"
        
    def set_cards(self,cards):
        self.cards = cards
        
    def set_seat(self,seat):
        self.seat = seat
        
    def set_money(self,money):
        self.money = money
        



class Card:
    def __init__(self,number,suit):
        self.number = number
        self.suit = suit
        
        
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["spades","clubs","diamonds","hearts"]:
            for i in range(1,14):
                if i==1:
                    self.cards.append(Card("Ace",suit))
                    continue
                if i==11:
                    self.cards.append(Card("Jack",suit))
                    continue
                if i==12:
                    self.cards.append(Card("Queen",suit))
                    continue
                if i==13:
                    self.cards.append(Card("King",suit))
                    continue
                self.cards.append(Card(str(i),suit))
            
    def shuffler(self):
        indices = []
        for i in range(0,52):
            indices.append(i)        
        random_indices = []
        while len(indices) != 0:
            new_index = random.choice(indices)
            random_indices.append(new_index)
            indices.remove(new_index)
        new_cards = []
        for i in random_indices:
            new_cards.append(self.cards[i])
        self.cards = new_cards
            
        
        
                
        

class Table:
    def __init__(self,player_names,player_money):
        if len(player_names) != len(player_money):
            print("Number of players' names is different to the number of the different amounts of money that is allocated to them")
        self.shuffled_deck = Deck()
        self.shuffled_deck.shuffler()
        self.players = []
        for n in range(0,len(player_money)):
            self.players.append(Player(player_names[n],player_money[n]))
            self.players[n].set_seat(n+1)
            self.players[n].set_cards([self.shuffled_deck[n],self.shuffled_deck[n+len(player_money)]])
        
        
               
#t = Table(["Tazouli","Itzo","Damkaliaros","Austrekis"],[2000,2000,2000,2000])
#t.players[0].seat = 1
#t.players[0].cards = [Card("Ace","spades"),Card("Ace","clubs")]
#t.players[1].seat = 2
#t.players[1].cards = [Card("2","hearts"),Card("7","diamonds")]
#t.players[2].seat = 3
#t.players[2].cards = [Card("Jack","spades"),Card("Queen","diamonds")]
#t.players[3].seat = 4
#t.players[3].cards = [Card("5","clubs"),Card("King","clubs")]

#for c in t.shuffled_deck.cards:
#    print(c.number,c.suit)
    
#for p in t.players:
#    print(p.name,p.money,p.seat,[p.cards[0].number,p.cards[0].suit,p.cards[1].number,p.cards[1].suit])

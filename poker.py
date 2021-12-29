import random


class Player:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.cards = ["0","0"]
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
        self.pot = 0
        self.shuffled_deck = Deck()
        self.shuffled_deck.shuffler()
        self.players = []
        for n in range(0,len(player_money)):
            self.players.append(Player(player_names[n],player_money[n]))
            self.players[n].set_seat(n+1)
            #self.players[n].set_cards([self.shuffled_deck.cards(n),self.shuffled_deck.cards(n+len(player_money))])
    
    def set_pot(self,new_pot):
        self.pot = new_pot
        


def main():
    print("WELCOME YOU SONS OF BITCHES!!!")
    print("TO THE BEST POKER GAME THERE IS..")
    print("\n")
    print("Now, enter the number of the players please")
    number_of_players = int(input())
    print("Goooood!! And now enter their names")
    player_names = []
    for i in range(0,number_of_players):
        player_names.append(input())
    print("And their initial money please..")
    player_money = []
    for i in range(0,number_of_players):
        player_money.append(float(input()))
    table_of_hell = Table(player_names,player_money)
    players = table_of_hell.players
    deck = table_of_hell.shuffled_deck
    for n in range(0,len(players)):
        players[n].set_cards([deck.cards[n],deck.cards[n+number_of_players]])
    print("Name","Money","Seat","Cards")
    for p in players:
        print(p.name,p.money,p.seat,[p.cards[0].number,p.cards[0].suit,p.cards[1].number,p.cards[1].suit])

    print("\n")
    print("How many rounds would you like to play?")
    number_of_rounds = int(input())
    #for i in range(1,number_of_rounds):
   
    
    
main()    
               
        
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

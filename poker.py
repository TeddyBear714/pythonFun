import random


class Player:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.cards = ["0","0"]
        self.seat = "0"
        self.active = True
        self.bet = 0
        
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
    def __init__(self,player_names,player_money,small,big):
        if len(player_names) != len(player_money):
            print("Number of players' names is different to the number of the different amounts of money that is allocated to them")
        self.pot = 0
        self.small_blind = small
        self.big_blind = big
        self.common_cards = [Card("Joker","clubs"),Card("Joker","clubs"),Card("Joker","clubs"),Card("Joker","clubs"),Card("Joker","clubs")]
        self.shuffled_deck = Deck()
        self.shuffled_deck.shuffler()
        self.players = []
        self.to_call = "False"
        self.raiser = None
        self.raise = 0
        for n in range(0,len(player_money)):
            self.players.append(Player(player_names[n],player_money[n]))
            self.players[n].set_seat(n+1)
            #self.players[n].set_cards([self.shuffled_deck.cards(n),self.shuffled_deck.cards(n+len(player_money))])
    
    def set_pot(self,new_pot):
        self.pot = new_pot
        
    def set_common_cards(self,common_cards):
        self.common_cards = common_cards
        
        
        


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
    
    
    #From here and beyond I should cut the code into a new "next_round" method in the Table class
    deck = table_of_hell.shuffled_deck
    for n in range(0,len(players)):
        players[n].set_cards([deck.cards[n],deck.cards[n+number_of_players]])
    common_cards = deck.cards[2*number_of_players:3+(2*number_of_players)]+[deck.cards[(2*number_of_players)+4]]+[deck.cards[(2*number_of_players)+6]]
    table_of_hell.set_common_cards(common_cards)
    
    #======Before flop=====================================
    
    #Small and big blind
    players[0].money = players[0].money-table_of_hell.small
    players[1].money = players[1].money-table_of_hell.big
    table_of_hell.pot = table_of_hell.small + table_of_hell.big
    
    #Initial bets    
    for p in players:
        print(p.name," type 'c' to check, 'bx' to bet x chips or 'f' to fold")
        inp = input()
        if inp=="c":
            continue
        elif inp=="f":
            p.active = False
            continue
        splitted_input = inp.split("b")
        if splitted_input[0] != "":
            print("Cut the bullshit bruv")
        else:
            table_of_hell.to_call = True
            while table_of_hell.to_call == True:
                for defender in players.remove(p):
                    if defender

        #if nada:
            #"cut the bullshit"
        #else:
            #to_call = True
            #while table_of_hell.to_call == True:
                 #for defence in players.remove(attacker):
                        #if defender raises
                            #attacker = defender
                            #break
                        #else
                            #
        

         #
          #  if input() == "c":
           #     continue
            #elif input() == "f":
             #   defender.active == False
              #  continue
            #splitted_input = input().split("b")
            #if splitted_input[0] != "":
             #   print("Cut the bullshit mate..")
            #else:
             #   bet = float(splitted_input[1])
              #  table_of_hell.pot = table_of_hell.pot + bet
               # table_of_hell.to_call = True
               # table_of_hell.raiser = defender
                #attacker = players.index(p)
    
    #better add it as a method in Table
    
    
 #   sMin = players[0].seat
  #  end = False
   # while end==False:
    #    if p.seat <= sMin
     #   sorted_players.append(p)
      #  sMin = p.seat
        
        
    
    print("Name","Money","Seat","Cards")
    for p in players:
        print(p.name,p.money,p.seat,[p.cards[0].number,p.cards[0].suit,p.cards[1].number,p.cards[1].suit])
    
    print("Flop:")
    print([[x.number,x.suit] for x in common_cards[0:3]])
    print("Turn")
    print(common_cards[3].number,common_cards[3].suit)
    print("River")
    print(common_cards[4].number,common_cards[4].suit)

    
    
    
    print("\n")
    print("How many rounds would you like to play?")
    number_of_rounds = int(input())
    #for i in range(1,number_of_rounds):
   
    


#main()    

#sorter
a = [2,3,-2,20,4,0,6]
aInit = a
print("This is a")
print(aInit)
#index = []
aSorted = []
while len(a)!=0:
    minim = a[0]
    index0 = 0
    for j in range(0,len(a)):
        if a[j]<=minim:
            minim = a[j]
            index0 = j
    aSorted.append(a[index0])
    a.remove(a[index0])

#for i in range(0,len(a)):
 #   aSorted.append(a[index[i]])

print("This is aSorted")
print(aSorted)
        
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

#print("Name","Money","Seat","Cards")
#for p in players:
#    print(p.name,p.money,p.seat,[p.cards[0].number,p.cards[0].suit,p.cards[1].number,p.cards[1].suit])

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
        self.active_players = []
        self.to_call = False
        self.end_of_hand = False
        for n in range(0,len(player_money)):
            self.players.append(Player(player_names[n],player_money[n]))
            self.players[n].set_seat(n+1)
            #self.players[n].set_cards([self.shuffled_deck.cards(n),self.shuffled_deck.cards(n+len(player_money))])
    
    def set_pot(self,new_pot):
        self.pot = new_pot
        
    def set_common_cards(self,common_cards):
        self.common_cards = common_cards
            
    def action(self):        
        players = [act for act in self.active_players]                  
                
        #Initial bets    
        for p in players:
            print(p.name," type 'c' to check, 'bx' to bet x chips or 'f' to fold")
            inp = input()
            if inp=="c":
                continue
            elif inp=="f":
                p.active = False
                if players.index(p) == (len(players)-2):
                    break
                else:
                    continue
            splitted_input = inp.split("b")
            if splitted_input[0] != "":
                print("Cut the bullshit bruv")
            else:
                table_of_hell.to_call = True
                attacker = p    #That's the player that initiates a bet
                attacker_bet = p.bet + float(splitted_input[1])  #That's the total amount of money that the attacker has placed in the pot
                p.money = p.money - float(splitted_input[1])
                p.bet = attacker_bet
                table_of_hell.pot = table_of_hell.pot + float(splitted_input[1])

                while table_of_hell.to_call == True:

                    active_defence_players = []
                    for act_def in players:
                        if act_def.active == True:
                            active_defence_players.append(act_def)
                    active_defence_players.remove(attacker)
                    
                    #defenders are all the players that need to match a bet by an attacker

                    for defender in active_defence_players:
                        amount_to_call = attacker_bet - defender.bet
                        print(defender.name," you need ",amount_to_call," to call")
                        print("Press 'cl' to call, 'f' to fold or 'rx' to raise to x money")
                        defender_input = input()
                        if defender_input == "cl":
                            defender.bet = attacker_bet #The TOTAL amount of money that this defender has placed in the pot so far
                            defender.money = defender.money - amount_to_call
                            table_of_hell.pot = table_of_hell.pot + amount_to_call
                            #That is to check if this defender is the last one to speak
                            #If yes, the loop ends since all the attacks have been matched either by a call or a fold
                            if active_defence_players.index(defender) == (len(active_defence_players)-1): 
                                table_of_hell.to_call = False
                        elif defender_input == "f":
                            defender.active = False
                            if active_defence_players.index(defender) == (len(active_defence_players)-1):
                                table_of_hell.to_call = False
                        else: 
                            #In this case, this defender becomes the new attacker
                            #and the while loop starts from the beginning
                            #since everyone that is still active needs to match this new attack
                            splitted_input_def = defender_input.split("r")
                            if splitted_input_def[0] != "":
                                print("Cut the bullshit bruv!")
                            else:
                                defender.bet = defender.bet + float(splitted_input_def[1])
                                defender.money = defender.money - float(splitted_input_def[1])
                                table_of_hell.pot = table_of_hell.pot + float(splitted_input_def[1])
                                attacker = defender
                                attacker_bet = defender.bet
                                break
                break

        for pla in players:            
            if pla.active == False:                
                self.active_players.remove(pla)                    
        if len(self.active_players) == 1:
            self.end_of_hand = True            


    

        
       
        
        
        


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
    table_of_hell = Table(player_names,player_money,1,2)
    players = table_of_hell.players
    for act_player in players:
        table_of_hell.append[act_player]
    
    #From here and beyond I should cut the code into a new "next_round" method in the Table class
    deck = table_of_hell.shuffled_deck
    for n in range(0,len(players)):
        players[n].set_cards([deck.cards[n],deck.cards[n+number_of_players]])
    common_cards = deck.cards[2*number_of_players:3+(2*number_of_players)]+[deck.cards[(2*number_of_players)+4]]+[deck.cards[(2*number_of_players)+6]]
    table_of_hell.set_common_cards(common_cards)
    
    #======Before flop=====================================
    #Small and big blind
    players = table_of_hell.players
    players[0].money = players[0].money-table_of_hell.small_blind
    players[0].bet = table_of_hell.small_blind
    players[1].money = players[1].money-table_of_hell.big_blind
    players[1].bet = table_of_hell.big_blind
    table_of_hell.pot = table_of_hell.small_blind + table_of_hell.big_blind
    #Players' actions
    table_of_hell.action()
    
    #======Flop============================================
    if table_of_hell.end_of_hand == False:
        print(" ")
        print("Flop is")
        print([[x.number,x.suit] for x in common_cards[0:3]])
        
        #======Before turn=================================
        table_of_hell.action()
        
        #======Turn========================================
        if table_of_hell.end_of_hand == False:
            print(" ")
            print("Turn is")
            print([common_cards[4].number,common_cards[4].suit])
            
            #======Before river============================
            table_of_hell.action()
            
            #======River===================================
            if table_of_hell.end_of_hand == False:
                print(" ")
                print("River is")
                print([common_cards[5].number,common_cards[5].suit])

                
    print("Active players are ",[p.name for p in active_players])
    print(" ")
    print("Table's pot is ",table_of_hell.pot)
    print(" ")
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
   
    


main()    

#sorter
#a = [2,3,-2,20,4,0,6]
#aInit = a
#print("This is a")
#print(aInit)
#index = []
#aSorted = []
#while len(a)!=0:
#    minim = a[0]
 #   index0 = 0
#    for j in range(0,len(a)):
#        if a[j]<=minim:
#            minim = a[j]
#            index0 = j
#    aSorted.append(a[index0])
#    a.remove(a[index0])

#for i in range(0,len(a)):
 #   aSorted.append(a[index[i]])

#print("This is aSorted")
#print(aSorted)
        
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

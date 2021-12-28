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
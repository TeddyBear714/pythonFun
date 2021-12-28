class Player:
    def __init__(self,name,seat,money):
        self.name = name
        self.seat = seat
        self.money = money
        
    def set_cards(self,cards):
        self.cards = cards
        
    def set_seat(self,seat):
        self.seat = seat
        
    def set_money(self,money):
        self.money = money
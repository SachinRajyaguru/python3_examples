class Player:
    
    def __init__(self,num_):
        self.name = input('Enter Your Name(def:blank)  :- ') or f'Player {num_}'
        self.cards = [None,None,None]
        
    def get_name(self):
        return self.name
    
    def set_card(self,card_index,card_value):
        self.cards[card_index] = card_value
    
    def print_boot(self):
        print(f'{self.name} has {self.cards}')

    def get_boot(self):
    	return self.cards

import random

player_number = int(input("HOW MANY PLAYER(s) Will Be Play :- "))

cards = []
for card_type in ('♦','♣','♥','♠'):
    for number in ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'):
        cards.append(f'{number}{card_type}')

ply_list = [Player(i) for i in range(player_number)]

for player in ply_list:
    for i in range(3):
        random_card = random.choice(cards)
        cards.remove(random_card)
        player.set_card(i,random_card)

for player in ply_list:
	player.print_boot()
    
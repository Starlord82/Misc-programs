#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Sum function with *args to sum the total, check if theres an ace
import random
from os

ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
values = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
        '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 1} 
class Card:
    
    def __init__(self,rank):
        self.rank = rank
        self.values = values[rank]
        
    def __str__(self):
        return self.rank
    
    def __rpr__(self):
        return self.rank

class Deck:
    
    def __init__(self):
        self.all_cards = []
        for suit in range(4):
            for rank in ranks:
                self.all_cards.append(Card(rank))
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        
    def deal(self):
        return self.all_cards.pop(0)
###############################################
class Player:
    
    def __init__(self,name = 'Player',deposit = 100):
        self.name = name
        self.deposit = deposit
        self.hand = Hand()
        
    def place_bet(self):
        while True:
            try:
                bet = int(input('Please enter bet amount: '))
            except:
                print('It looks like you have entered an invalid bet amount, please try again')
                continue
            if player.check_funds(bet):
                self.deposit -= bet
                print(f'You are left with {self.deposit}$!')
                break
            else:
                print('Insufficient funds!')
                print(player)
                continue
        return bet
        
    def check_funds(self,bet):
        if bet <= self.deposit:
            return True
        else:
            return False
            
    def win(self):
        self.deposit += bet * 2
        print(f'You have won {bet*2}$')
        print(f'You now have {self.deposit}$!')
        
    def show_dealer(self):
        print(f'{self.hand.cards[0]} x')

    def __str__(self):
        return (f'You have {self.deposit}$')
###############################################            
class Hand:
    
    def __init__(self):
        self.cards = []
        
    def hit(self,deck):
        self.cards.append(deck.deal())
        
    def hand_sum(self):
        total = 0
        is_a = False
        for card in self.cards:
            if card.rank == 'A' and not(is_a):
                is_a = True
                continue
            else:
                total += card.values
        if is_a:
            if total <= 10:
                total += 11
            else:
                total += 1
        return total
    
    def is_busted(self):
        
        if self.hand_sum() > 21:
            return True
        else:
            return False


    def __str__(self):
        return " ".join(map(str, self.cards))
###############################################    

        
def dealer_turn(dealer,bet):
    os.system("cls")
    print('Dealers turn!\n')
    while True:
        
        print("Dealer hand:")
        print(dealer.hand)
        print("Your hand:")
        print(player.hand)
        if dealer.hand.is_busted():
            print("Dealer busted, you win!")
            player.win()
            break
        elif dealer.hand.hand_sum() > player.hand.hand_sum():
            print("You lose, Dealer wins!")
            print(player)
            break
        else:
            dealer.hand.hit(deck)
            print('Dealer Hits')
            
                
def player_turn(player):
    actions = ['H','','S','s','h']
    while True:
        
        action = input('H or "enter" to hit\nS to stay\n') 
        if action not in actions:
            print("Invalid choice!")
            continue
        elif action in ['S','s']:
            return player.hand.cards
        else:
            player.hand.hit(deck)
        os.system("cls")
        print("Dealer hand:")
        dealer.show_dealer()
        print("Your hand:")
        print(player.hand)
        if player.hand.is_busted():
            return "Busted"
            
def new_game(mode):
    
    if mode == "continue?":    
        while True:
                c = input("Continue? (y/n): ")
                if c not in ('y','n','Y','N'):
                    print('y ot n please.')
                    continue
                else:
                    break

        if c in ['y','Y']:
            return True
        elif c in ['n','N']:
            print('Thanks for playing!')
            return False
        
    elif mode == "new game?":
    
        while True:
                new_game = input('New Game? (y/n): ')
                if new_game not in ('y','n','Y','N'):
                    print('y or n please.')
                    continue
                else:
                    break  
        if new_game in ['Y','y']:
            return True
        else:
            return False


# In[14]:


deck = Deck()
deck.shuffle_deck()
player = Player()
dealer = Player()
game_on = True

player
print("""Welcome to the game of BlackJack!\nYou start with 100$ of funds, and each round you decide your bet amount.
      \nIf you lose, you lose the bet, if you win, you get rewarded with you're bet doubled.\nGood Luck!""")


# In[15]:


while game_on:
    funds = True
    player = Player()
    dealer = Player()
    
    while funds:
        deck = Deck()
        deck.shuffle_deck()
        player.hand.cards = []
        dealer.hand.cards = []
    
        bet = player.place_bet()
        print("\n")
        player.hand.all_cards = [player.hand.hit(deck) for x in range(2)]
        dealer.hand.all_cards = [dealer.hand.hit(deck) for x in range(2)]
        print("Dealer hand:")
        dealer.show_dealer()
        print("Your hand:")
        print(player.hand)
        player.hand.cards = player_turn(player)
        
        if player.hand.cards == "Busted":
            print("Busted! You lose!")
            print(player)
            funds = new_game("continue?")
            if not funds:
                game_on = new_game("new game?")
            if player.deposit <= 0:
                print('Looks like you are out of money\nGAME OVER!')
                funds = False
                game_on = new_game("new game?")
                
        else:
            dealer_turn(dealer,bet)
            if player.deposit <= 0:
                print('Looks like you are out of money\nGAME OVER!')
                funds = False
                game_on = new_game("new game?")
                break
            funds = new_game("continue?")
            if not funds:
                game_on = new_game("new game?")

       


# In[ ]:





# In[ ]:





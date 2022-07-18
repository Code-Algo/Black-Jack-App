from curses.ascii import isalpha
import sys
#from pyparsing import alphas
import pyfiglet
import colorama 
import requests
import ascii_magic
import random
import os
import time
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


class BlackJack():
    def __init__(self):
        
        self.deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','K','Q','A','J','K','Q','A','J','K','Q','A','J','K','Q','A']
    #self.deck = [{'spades':2,'spades':3,'spades':4,'spades':5,'spades':6,'spades':7,'spades':8,'spades':9,'spades':10,'clubs':2,'clubs':3,'clubs':4,'clubs':5,'clubs':6,'clubs':7,'clubs':8,'clubs':9,'clubs':10,'hearts':2,'hearts':3,'hearts':4,'hearts':5,'hearts':6,'hearts':7,'hearts':8,'hearts':9,'hearts':10,'diamonds':2,'diamonds':3,'diamonds':4,'diamonds':5,'diamonds':6,'diamonds':7,'diamonds':8,'diamonds':9,'diamonds':10,'diamonds':'J','diamonds':'K','diamonds':'Q','diamonds':'A','hearts':'J','hearts':'K','hearts':'Q','hearts':'A','clubs':'J','clubs':'K','clubs':'Q','clubs':'A','spades':'J','spades':'K','spades':'Q','spades':'A'}]
        self.player_deck = []
        self.dealer_deck = []
        self.face = ['J','K','Q']
        self.ace = ['A']
        self.player_in = True
        self.dealer_in = True
    
    def dealer_hand(self):
        card = random.choice(self.deck)
        self.dealer_deck.append(card) 
        return self.dealer_deck
    
    def player_hand(self):
        card = random.choice(self.deck)
        self.player_deck.append(card) 
        return self.player_deck #self.deck

    def player_points(self):

        self.p_points = 0
        #self.face = ['J','K','Q']
        for card in self.player_deck:
            if card in range(11):
                self.p_points += card
            if card in self.face:
                 self.p_points += 10
            if card in self.ace:
                if  self.p_points > 11:
                        self.p_points += 1
                if  self.p_points < 11:
                        self.p_points += 11
        return self.p_points#self.p_points

    def dealer_points(self):

        self.d_points = 0

        for card in self.dealer_deck:
            if card in range(11):
                self.d_points += card
            if card in self.face:
                self.d_points += 10
            if card in self.ace:
                if self.d_points > 11:
                    self.d_points += 1
                if self.d_points < 11:
                    self.d_points += 11
        return self.d_points#self.d_points
    
    def welcome_screen(self):
        self.clear_screen()
        print('\n'*5)
        logo = ascii_magic.from_image_file('black_jack_title.jpg', columns = 50)
        ascii_magic.to_terminal(logo)
        print('\n'*2)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_dealer_deck(self):
        if len(self.dealer_deck) == 2:
            return self.dealer_deck[0]
        if len(self.dealer_deck) > 2:
            return self.dealer_deck [0], self.dealer_deck[1]

black = BlackJack()
def main():
    black.welcome_screen()
    time.sleep(1)
    prompt = input(f"{Fore.RED}{Style.BRIGHT}Welcome to BlackJack! Press 1 for a seat. ")
    if prompt == '1':
        time.sleep(1)
        seat = ascii_magic.from_image_file('seat.jpg', columns = 50)
        ascii_magic.to_terminal(seat)
        time.sleep(2)
        print(f"{Fore.RED}{Style.BRIGHT}\nDealer Hand: {black.dealer_hand()}")
        print(f"{Fore.WHITE}{Style.BRIGHT}\nYour Hand: {black.player_hand()}")
        black.dealer_hand()
        black.player_hand()
        #print(f"Dealer Hand: {black.dealer_draw()} Dealer Points: {black.dealer_points()}")
       # print(f"Your Hand: {black.player_draw()} Your Points: {black.player_points()}")
    while black.player_in or black.dealer_in:
            print(f"{Fore.RED}{Style.BRIGHT}\nDealer Hand: {black.show_dealer_deck()} and ?. Dealer Points: {black.dealer_points()} ")
            print(f"{Fore.WHITE}{Style.BRIGHT}\nYour Hand: {black.player_deck}. Your Points: {black.player_points()}")
            if black.player_in:
                prompt_two = input(f"{Fore.YELLOW}{Style.BRIGHT}\nPress 1 to Hit. Press 2 to Stay. ")
            if black.d_points > 16:
                black.dealer_in = False
            else:
                black.dealer_hand()
            if prompt_two == '2':
                black.player_in = False
                #if black.p_points == black.d_points:
                    #print("Draw, Coward!")
                #elif black.d_points > black.p_points:
                    #("You Lose, Coward!")
                    #break
            else:
                black.player_hand()
                #print(f"Dealer Hand: {black.dealer_deck} Dealer Points: {black.dealer_points()}")
                #print(f"Your Hand: {black.player_hand()} Your Points: {black.player_points()}")
            if black.p_points >= 21:
                break
            elif black.d_points >= 21:
                break
    if black.p_points == 21:
        result = pyfiglet.figlet_format("BlackJack! You Win!", font = "epic")
        print(result)
    elif black.d_points == 21:
        result = pyfiglet.figlet_format(f"Dealer Had: {black.dealer_deck}. BlackJack! Dealer Wins!", font = "larry3d")
        print(result)
    elif black.p_points > 21:
        result = pyfiglet.figlet_format("You Bust loser! Dealer Wins!", font = "doom")
        print(result)
    elif  black.d_points > 21:
        result = pyfiglet.figlet_format(f"Dealer Had: {black.dealer_deck}. Dealer Busts! You Win!", font = "larry3d")
        print(result)
    elif 21 - black.d_points < 21 - black.p_points:
        result = pyfiglet.figlet_format(f"Dealer Had: {black.dealer_deck}. Dealer Wins!", font = "larry3d")
        print(result)
    elif 21 - black.d_points > 21 - black.p_points:
        result = pyfiglet.figlet_format("You Win!", font = "epic")  
        print(result)
            
            
            
    #print(black.dealer_hand())
    #print(black.player_hand())
    #print(black.player_points())
    #print(black.dealer_points())
    #print(black.player_draw())
    #print(black.player_points())
    #print(black.dealer_draw())
    #print(black.dealer_points())
   

main()
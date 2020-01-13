import random
import sys
from character import Character
from phrase import Phrase
player_phrase = []
class Game:
    
    #def __init__(self, phrases):
        #self.phrases = phrases
        
    def game_menu(self):
        print('Welcome to Phrase Hunter!')
        print('-' * 43)
        print('Please enter "S" to (START).')
        print('Please enter "E" to (EXIT).')
        print('Please enter "Q" to (QUIT) current session.')
        return '-' * 43
    
    def game_loop(self):
        menu_interface = input('Please enter a letter from the game menu: ')
        if menu_interface.upper() == 'S':
            player_answers = []
            player_name = input('Please enter your name: ')
            player_phrase = Phrase(player_answers)
            print(player_phrase.phrase_ghost())
            while True:
                
                player_letter = input('{}, please enter a letter from (A-Z): '.format(player_name))
                 
                player_character = Character(player_letter)
                 
                if len(player_letter.upper()) == 1:
                    player_answers.append(player_letter)
                    
                    print(player_character.guess_letter())
                    print(player_character.reveal_letter())
                    print(player_phrase.phrase_reveal())
                     
                else:
                    print('Please enter one letter at a time')
                
        elif menu_interface.upper() == 'E':
            sys.exit('Thank you for playing!')
                
                
        elif menu_interface.upper() == 'Q':
            print('Player must be in game to quit.')
                
        else:
            print('Please enter "S" or "E" to proceed.')
        

#player_character = Character()
#player_phrase = Phrase()
game_phrase = Game()

print(game_phrase.game_menu())
print(game_phrase.game_loop())
 
# need to define char, phrase and phrases

#phrases needs to hold the random word

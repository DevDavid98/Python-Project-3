import random
import sys
from character import Character
from phrase import Phrase
phrases = []
class Game:

    def __init__(self, phrases):
        
        self.phrases = phrases
        
    def game_menu(self):
        
        print('Welcome to Phrase Hunter!')
        print('-' * 43)
        print('Please enter "S" to (START).')
        print('Please enter "E" to (EXIT) within game menu.')
        return '-' * 43
    
    def game_loop(self):
        while True:
            menu_interface = input('Please enter a letter from the game menu: ')
            print('-' * 43)
            if menu_interface.upper() == 'S':
                
                player_answers = []
                
                player_name = input('Please enter your name: ')
                

                player_phrase = Phrase(player_answers)
                
                phrases.append(player_phrase.phrase_ghost())

                player_lives = 5
                while True:

                    player_letter = input('{}, please enter a letter from (A-Z): '.format(player_name)).upper()
                    player_character = Character(player_letter)

                    if len(player_letter) == 1:

                        player_answers.append(player_letter)

                        print(player_character.guess_letter())
                                              
                        print(player_character.reveal_letter())

                        print(player_phrase.phrase_reveal())              
                        if player_letter.upper() in player_phrase.random_word.upper():
                            print('-' * 43)
                            print('The letter "{}" is correct!.'.format(player_letter))
                            
                        elif player_letter.upper() != player_phrase.random_word.upper():
                            player_lives -= 1
                            print('-' * 43)
                            print('{}, you have {} lives!'.format(player_name,player_lives))
                        
                        if "_" not in player_phrase.phrase_ghost:
                            print('All letters guessed, YOU WIN!')
                            print('*' * 43)
                            break
                            
                        if player_lives == 0:
                            print('GAME OVER, YOU LOSE!')
                            print('*' * 43)
                            break

                    else:
                        print('Please enter one letter at a time')      
            elif menu_interface.upper() == 'E':
                sys.exit('Thank you for playing!')    
            else:
                print('Please enter "S" or "E" to proceed.')
                

game_phrase = Game(phrases)
print(game_phrase.game_menu())
print(game_phrase.game_loop())

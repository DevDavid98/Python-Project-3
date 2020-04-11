# imports modules and files to the game.py file
import random
import sys
from character import Character
from phrase import Phrase

# stores the phrase_ghost from phrase.py
phrases = []

# All the for the game
the_answers = ['David', 'Carly', 'Sarina', 'Playstation',
               'Android', 'Anime', 'Cash', 'Music', 'Videos',
               'Games', 'CPU', 'GPU', 'Motherboard', 'RAM', 'SSD',
               'BIOS', 'Python', 'Programming', 'Treehouse',
               'Guitar', 'Kratos', 'Atreus', 'Hero', 'Goku', 'Deku',
               'Naruto', 'Vegeta', 'Aloy', 'CJ']


class Game:

    # initalizes the phrases object which is the phrase_ghost
    def __init__(self, phrases):

        self.phrases = phrases

    # starts the game menu
    def game_menu(self):

        print('Welcome to Phrase Hunter!')
        print('-' * 43)
        print('Please enter "S" to (START).')
        print('Please enter "E" to (EXIT) within game menu.')
        return '-' * 43

    def game_loop(self):

        # starts the game loop for the player
        while True:
            menu_interface = input('Enter a letter from the game menu: ')
            print('-' * 43)

            if menu_interface.upper() == 'S':

                # this is the phrase parameter
                player_answers = []

                player_name = input('Please enter your name: ')

                # This is the Phrase class object with two parameters
                player_phrase = Phrase(the_answers, player_answers)

                phrases.append(player_phrase.phrase_ghost())

                player_lives = 10

                while True:

                    player_letter = input('{}, enter a letter from (A-Z): '
                                          .format(player_name)).upper()

                    # makes sure only letters are guessed
                    if player_letter.isalpha():

                        # This is the Character object that take one parameter
                        player_character = Character(player_letter)

                        # Makes sure the player only guesses one at a time
                        if len(player_letter) == 1:
                            player_answers.append(player_letter)

                            print(player_character.guess_letter())

                            print(player_character.reveal_letter())
                            print(player_phrase.phrase_reveal())

                            # Tells the player the letter is correct if right.
                            if player_letter.upper() in \
                                    player_phrase.random_word.upper():

                                print('-' * 43)
                                print('The letter "{}" is correct!.'
                                      .format(player_letter))

                            # Tells the player the guess was wrong
                            elif player_letter.upper() != \
                                    player_phrase.random_word.upper():

                                player_lives -= 1
                                print('-' * 43)
                                print('{}, you have {} lives!'
                                      .format(player_name, player_lives))

                            # Tells the player they have won
                            if "_" not in player_phrase.phrase_ghost:

                                print('All letters guessed, YOU WIN!')
                                del player_character.original[:]
                                print('*' * 43)
                                break

                            # Tells the player they have lost
                            if player_lives == 0:

                                print('GAME OVER, YOU LOSE!')
                                print('Your Phrase was ({})!'
                                      .format(player_phrase.random_word))
                                del player_character.original[:]
                                print('*' * 43)
                                break

                        else:
                            print('Please enter one letter at a time')
                    else:
                        print('Please enter letters only.')

            elif menu_interface.upper() == 'E':
                sys.exit('Thank you for playing!')

            else:
                print('Please enter "S" or "E" to proceed.')

# This is the game object that has one parameter
game_phrase = Game(phrases)

# This Basically starts the whole game
print(game_phrase.game_menu())
print(game_phrase.game_loop())

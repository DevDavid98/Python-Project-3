# imports the Character class from the file character.py
from character import Character

# imports random module
import random


class Phrase:
    # initalizes the the class with two parameters
    def __init__(self, phrase, player_answers):
        self.phrase = phrase
        self.player_answers = player_answers

    # this method randomizes the self.phrase object,
    # that have the answers the_answers.
    # outputs the randomized word with underscores
    def phrase_ghost(self):
        # store this within phrase
        self.random_word = random.choice(self.phrase)
        self.phrase_ghost = ['_ '] * len(self.random_word)
        return ''.join(self.phrase_ghost)

    # This method reveals the underscores from phrase_ghost
    # if guessed correctly
    def phrase_reveal(self):
        count = 0
        for index, letter in enumerate(self.random_word):
            if letter.upper() in self.player_answers:
                count += 1
                self.phrase_ghost.insert(count-1, letter.upper())
                self.phrase_ghost.pop(count)
                if count == len(self.random_word):
                    return ' '.join(str(e) for e in self.phrase_ghost)
            else:
                count += 1
                self.phrase_ghost.insert(count-1, '_')
                self.phrase_ghost.pop(count)
                if count == len(self.random_word):
                    return ' '.join(str(e) for e in self.phrase_ghost)

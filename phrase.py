from character import Character
import random

class Phrase:
    the_answers = ['David', 'Carly', 'Sarina', 'Playstation', 'Android', 'Anime', 'Cash', 'Music', 'Videos', 
                   'Games', 'CPU', 'GPU', 'Motherboard', 'RAM', 'SSD', 'BIOS', 'Python', 'Programming', 'Treehouse']
    def __init__(self, phrase):
        self.phrase = phrase

    def phrase_ghost(self):
        self.random_word = random.choice(self.the_answers)
        self.phrase_ghost = ['_ '] * len(self.random_word)
        return ''.join(self.phrase_ghost)
    
    def phrase_reveal(self):
        count = 0
        for index, letter in enumerate(self.random_word):
            if letter.upper() in self.phrase:
                count += 1
                self.phrase_ghost.insert(count-1,letter.upper())
                self.phrase_ghost.pop(count)
                if count == len(self.random_word):
                    return ' '.join(str(e) for e in self.phrase_ghost)
            else:
                count += 1
                self.phrase_ghost.insert(count-1,'_')
                self.phrase_ghost.pop(count)
                if count == len(self.random_word):
                    return ' '.join(str(e) for e in self.phrase_ghost)

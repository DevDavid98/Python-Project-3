class Character:
    original = []
    def __init__(self, char, was_guessed = False):
        self.char = char
        self.was_guessed = False

    def guess_letter(self):
        self.original.append(self.char)
        
        if self.char in self.original:
            self.was_guessed = True
            return ''

        else:
            self.was_guessed = False
            
    def reveal_letter(self):
        if self.was_guessed == True:
            return ' '.join(self.original)


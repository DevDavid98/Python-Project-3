class Character:
    original = []
    def __init__(self, char, was_guessed = False):
        self.char = char
        self.was_guessed = False

    def guess_letter(self):
        if self.char not in self.original:
            self.original.append(self.char)
            return ''
        
        elif self.char in self.original:
            self.was_guessed = True

    def reveal_letter(self):
        print('Your recently guessed letter: {}'.format(' '.join(self.original)))
        del self.original[:]
        return ''
        if self.was_guessed == True:
            print('')
            return 'The letter, "{}" is already guessed.'.format(' '.join(self.char))

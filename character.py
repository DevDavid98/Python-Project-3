class Character:

    # stores the original letter guessed to be used in comparison.
    original = []

    # starts the class with two parameters with char storing a letter.
    def __init__(self, char, was_guessed=False):

        self.char = char
        self.was_guessed = False

    # this method stores letters in the original list
    # also checks if letter was guessed
    def guess_letter(self):
        if self.char not in self.original:
            self.original.append(self.char)
            return ''

        elif self.char in self.original:
            self.was_guessed = True
            return ''

    # This method shows you the letters guessed
    # also tells the player if the letter was guessed
    def reveal_letter(self):
        print('Your recently guessed letters: {}'
              .format(' '.join(self.original)))

        if self.was_guessed is True:
            print('The letter, "{}" is already guessed.'
                  .format(' '.join(self.char)))
        return ''

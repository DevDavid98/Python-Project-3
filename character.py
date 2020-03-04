class Character:
    original = []

    def __init__(self, char, was_guessed=False):

        self.char = char
        self.was_guessed = False

    def guess_letter(self):
        if self.char not in self.original:
            self.original.append(self.char)
            return ''

        elif self.char in self.original:
            self.was_guessed = True
            return ''

    def reveal_letter(self):
        print('Your recently guessed letters: {}'
              .format(' '.join(self.original)))

        if self.was_guessed is True:
            print('The letter, "{}" is already guessed.'
                  .format(' '.join(self.char)))
        return ''

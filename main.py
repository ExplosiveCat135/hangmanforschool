import random

words = []

HANGMANPICS = [
    '''







    ''',
    '''







    =========
    ''',
    '''
        +
        |
        |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
        |
        |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
        |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========
    ''']


with open('dictionary.txt') as f:
    for line in f:
        words.append(line.strip())

class Game:
    def __init__(self, word=None):
        self.word = word if word else random.choice(words)
        self.wordstate = ['_' for _ in self.word]
        self.hangmanstate = 0
        self.lettersguessed = []

    def guess(self, letter):
        if letter in self.word:
            if letter not in self.wordstate:
                for i, l in enumerate(self.word):
                    if l == letter:
                        self.wordstate[i] = letter
                self.lettersguessed.append(letter)
            elif letter in self.wordstate or letter in self.lettersguessed:
                print('Letter already guessed. Try again.')
        else:
            print('Letter not in word. Try again.')
            self.hangmanstate += 1

    def printwordstate(self):
        print(' '.join(self.wordstate))

    def printgame(self):
        print(HANGMANPICS[self.hangmanstate])
        self.printwordstate()
        print('Letters guessed: ' + ' '.join(self.lettersguessed))


def main():
    game = Game("hello")
    print('Welcome to Hangman!')
    input('Press ENTER to start the game.')
    while True:
        print("---------------------")
        if game.hangmanstate == 10:
            game.printgame()
            print('You lose! The word was ' + game.word)
            break
        elif "_" not in game.wordstate:
            print('You win! The word was ' + game.word)
            break
        game.printgame()
        playerguess = input('Guess a letter: ')
        while len(playerguess) != 1 or not playerguess.isalpha():
            playerguess = input('Invalid input. Guess a single letter: ')
        game.guess(playerguess.lower())
    if input('Play again? (y/n) ') == 'y':
        main()

if __name__ == '__main__':
    main()

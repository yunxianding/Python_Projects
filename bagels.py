import random

NUM_DIGITS = 3
MAX_GUESSES = 10


class BagelsGame:
    def __init__(self, level=1, num_digits=None, max_guesses=None):
        self.level = max(1, int(level))

        if num_digits is None and max_guesses is None:
            self.num_digits, self.max_guesses = self.get_level_settings(self.level)
        else:
            if num_digits is None:
                num_digits = NUM_DIGITS
            if max_guesses is None:
                max_guesses = MAX_GUESSES

            if num_digits <= 0:
                raise ValueError('num_digits must be greater than zero.')
            if num_digits > 10:
                raise ValueError(
                    'num_digits cannot be greater than 10 because the game uses digits 0-9.'
                )
            if max_guesses <= 0:
                raise ValueError('max_guesses must be greater than zero.')

            self.num_digits = num_digits
            self.max_guesses = max_guesses

    @staticmethod
    def get_level_settings(level):
        level = max(1, int(level))
        num_digits = 3 + (level - 1)
        max_guesses = max(1, 10 - (level - 1) * 2)
        return num_digits, max_guesses

    def print_rules(self):
        print(
            '''
    Bagels, a deductive logic game.
    Adapted from Al Sweigart al@inventwithpython.com
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: Pico
    That means: one digit is correct but in the wrong position
    When I say: Fermi
    That means: one digit is correct and in the right position
    When I say: Bagels
    That means: No digit is correct
    '''.format(self.num_digits)
        )

    def get_secret_num(self):
        numbers = list('0123456789')
        random.shuffle(numbers)
        return ''.join(numbers[:self.num_digits])

    def validate_guess(self, guess):
        if guess is None:
            return None

        guess = str(guess).strip()

        if not guess:
            print('Please enter a value.')
            return None

        if len(guess) != self.num_digits:
            print('Please enter exactly {} digits.'.format(self.num_digits))
            return None

        if not guess.isdecimal():
            print('Please enter only numeric digits 0-9.')
            return None

        if len(set(guess)) != len(guess):
            print('Digits must be unique. No repeated digits allowed.')
            return None

        return guess

    def get_valid_guess(self, guess_number):
        while True:
            try:
                guess = input('Guess # {}: '.format(guess_number)).strip()
            except EOFError:
                print('\nInput closed. Exiting game.')
                raise SystemExit
            except KeyboardInterrupt:
                print('\nKeyboard interrupt detected. Exiting game.')
                raise SystemExit

            valid_guess = self.validate_guess(guess)
            if valid_guess is not None:
                return valid_guess

    def parse_yes_no(self, answer):
        normalized = str(answer).strip().lower()

        if normalized in {'y', 'yes'}:
            return True
        if normalized in {'n', 'no'}:
            return False
        return None

    def get_yes_no(self, prompt):
        while True:
            try:
                answer = input(prompt).strip()
            except (EOFError, KeyboardInterrupt):
                return False

            response = self.parse_yes_no(answer)
            if response is not None:
                return response
            print('Please answer yes or no.')

    def choose_level(self):
        while True:
            try:
                choice = input('Choose a difficulty level (1-5): ').strip()
                level = int(choice)
            except ValueError:
                print('Please enter a whole number from 1 to 5.')
                continue

            if 1 <= level <= 5:
                self.level = level
                self.num_digits, self.max_guesses = self.get_level_settings(level)
                print('Difficulty set to level {}.'.format(level))
                return level

            print('Level must be between 1 and 5.')

    def choose_next_action(self):
        while True:
            try:
                choice = input('Play again? [r] same level, [l] change level, [q] quit: ').strip().lower()
            except (EOFError, KeyboardInterrupt):
                return 'q'

            if choice in {'r', 'same', 's'}:
                return 'r'
            if choice in {'l', 'level', 'change'}:
                return 'l'
            if choice in {'q', 'quit', 'exit'}:
                return 'q'

            print('Please choose r, l, or q.')

    def play(self):
        print('Welcome to Bagels!')

        while True:
            try:
                self.choose_level()
                self.print_rules()

                secret_num = self.get_secret_num()
                print('I have thought up a number.')
                print('You have {} guesses to get it.'.format(self.max_guesses))

                for guess_number in range(1, self.max_guesses + 1):
                    guess = self.get_valid_guess(guess_number)
                    clues = get_clues(guess, secret_num)
                    print(clues)

                    if guess == secret_num:
                        print('You guessed it!')
                        break
                else:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(secret_num))

                action = self.choose_next_action()
                if action == 'q':
                    print('Thanks for playing!')
                    return
                if action == 'l':
                    continue

            except (EOFError, KeyboardInterrupt):
                print('\nGame interrupted. Exiting.')
                return
            except SystemExit:
                raise
            except Exception as exc:
                print(f'Unexpected error: {exc}')
                print('Restarting the game...')


def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for index, digit in enumerate(guess):
        if digit == secret_num[index]:
            clues.append('Fermi')
        elif digit in secret_num:
            clues.append('Pico')

    if not clues:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)


def main():
    game = BagelsGame()
    game.play()


if __name__ == '__main__':
    main()

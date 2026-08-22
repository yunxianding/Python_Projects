SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def hack_message(message):
    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in message:
            upper_symbol = symbol.upper()
            if upper_symbol in SYMBOLS:
                num = SYMBOLS.find(upper_symbol)
                num = num - key
                if num < 0:
                    num = num + len(SYMBOLS)
                decrypted_symbol = SYMBOLS[num]
                if symbol.isalpha() and symbol.islower():
                    decrypted_symbol = decrypted_symbol.lower()
                translated = translated + decrypted_symbol
            else:
                translated = translated + symbol
        print('Key # {}: {}'.format(key, translated))


def main():
    print('Caesar Cipher Hacker, adapted from Al Sweigart al@inevntwithpython.com')
    while True:
        print('Enter the encrypted Caesar cipher message to hack.')
        message = input('> ')
        hack_message(message)

        play_again = input('Hack another message? (Y/N): ').strip().upper()
        if play_again != 'Y':
            print('Goodbye!')
            break


if __name__ == '__main__':
    main()
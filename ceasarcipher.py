import string

try:
    import pyperclip
except ImportError:
    pyperclip = None

SYMBOLS = string.ascii_uppercase + string.digits + string.punctuation + ' '


def main():
    print('Caesar Cipher, adapted from Al Sweigart al@inventwithpython.com')
    print('The Caesar cipher encrypts letters by shifting them over by a')
    print('key number. For example, a key of 2 means the letter A is')
    print('encrypted into C, the letter B encrypted into D, and so on.')
    print()

    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').strip().lower()
        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break
        print('Please enter the letter e or d.')

    while True:
        max_key = len(SYMBOLS) - 1
        print(f'Please enter the key (0 to {max_key}) to use.')
        response = input('> ').strip()
        if not response.isdecimal():
            continue
        key = int(response)
        if 0 <= key < len(SYMBOLS):
            break

    print(f'Enter the message to {mode}.')
    message = input('> ').upper()
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            position = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                new_position = (position + key) % len(SYMBOLS)
            else:
                new_position = (position - key) % len(SYMBOLS)
            translated += SYMBOLS[new_position]
        else:
            translated += symbol

    print(translated)

    if pyperclip is not None:
        try:
            pyperclip.copy(translated)
            print(f'Full {mode}ed text copied to clipboard.')
        except Exception as exc:
            print(f'Could not copy to clipboard: {exc}')


if __name__ == '__main__':
    main()
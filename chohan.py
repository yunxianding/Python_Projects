import random

JAPANESE_NUMBERS = {1: 'ichi', 2: 'ni', 3: 'san', 4: 'shi', 5: 'go', 6: 'roku'}

STARTING_PURSE = 5000
COMPUTER_NAMES = ('A', 'B', 'C')


def get_bet(purse):
    """Ask for a legal wager and return its amount and prediction."""
    while True:
        try:
            bet = int(input(f'Enter an amount to bet (0 to quit, purse {purse}): '))
        except ValueError:
            print('Please enter a whole number.')
            continue
        if bet == 0:
            return 0, None
        if bet < 0:
            print('The amount must be 0 or more.')
        elif bet > purse:
            print('You do not have enough mon to make that bet.')
        else:
            break

    while True:
        guess = input('Bet on Cho, Han, or an exact number from 2 to 12: ').lower()
        if guess in ('cho', 'han'):
            return bet, guess
        try:
            number = int(guess)
        except ValueError:
            number = 0
        if 2 <= number <= 12:
            return bet, number
        print('Please enter "cho", "han", or a number from 2 to 12.')


def computer_bet(purse):
    """Give a computer gambler a legal wager."""
    bet = random.randint(1, min(purse, 500))
    prediction = random.choice(('cho', 'han', random.randint(2, 12)))
    return bet, prediction


def settle_bet(prediction, bet, total):
    """Return the net purse change for one prediction."""
    result = 'cho' if total % 2 == 0 else 'han'
    if prediction == result:
        multiplier = 1
    elif prediction == total:
        multiplier = 5
    else:
        return -bet

    if total == 7:
        multiplier += 1
    if total == 2:
        multiplier += 2
    return bet * multiplier


def describe_prediction(prediction):
    if isinstance(prediction, int):
        return f'exactly {prediction}'
    return prediction.title()


def play_round(players):
    bets = {}
    for player in players:
        if player['purse'] == 0:
            continue
        if player['human']:
            bet, prediction = get_bet(player['purse'])
            if bet == 0:
                return False
        else:
            bet, prediction = computer_bet(player['purse'])
            print(f"{player['name']} bets {bet} mon on {describe_prediction(prediction)}.")
        player['purse'] -= bet
        bets[player['name']] = (player, bet, prediction)

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    result = 'cho' if total % 2 == 0 else 'han'
    print(f'The dealer rolled {die1} and {die2} for a total of {total}: {result}.')
    if total == 7:
        print('Lucky seven! Winning bets receive an extra bet as a bonus.')
    elif total == 2:
        print('Snake eyes! Winning bets receive a triple-bet bonus.')

    for player, bet, prediction in bets.values():
        change = settle_bet(prediction, bet, total)
        player['purse'] += bet + change if change >= 0 else 0
        if player['human']:
            if change >= 0:
                print(f'You won {change} mon profit. Your purse is {player["purse"]} mon.')
            else:
                print(f'You lost {bet} mon. Your purse is {player["purse"]} mon.')
        else:
            outcome = f'won {change} mon profit' if change >= 0 else f'lost {bet} mon'
            print(f'{player["name"]} {outcome}; purse: {player["purse"]} mon.')
    return True


def main():
    print('''Cho-Han, adapted from Al Sweigart at inventwithpython.com
In this traditional Japanese dice game, gamblers bet on whether two dice total
an even (cho) or odd (han) number. You can also bet on the exact total.
Exact-number bets pay 5x profit; a 7 adds 1x and snake eyes adds 2x.''')
    players = [{'name': 'You', 'purse': STARTING_PURSE, 'human': True}]
    players.extend({'name': name, 'purse': STARTING_PURSE, 'human': False}
                   for name in COMPUTER_NAMES)

    while players[0]['purse'] > 0:
        print('\n' + ' | '.join(f"{p['name']}: {p['purse']} mon" for p in players))
        if not play_round(players):
            break
        players = [player for player in players if player['purse'] > 0 or player['human']]
        if players[0]['purse'] == 0:
            print('You are out of mon. Game over!')
            break
        again = input('Play another round? (y/n): ').lower()
        if again != 'y':
            break
    print(f"You leave with {players[0]['purse']} mon.")


if __name__ == '__main__':
    main()
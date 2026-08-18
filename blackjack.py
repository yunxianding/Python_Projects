import random
import sys

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print('''Blackjack, adapted from Al Sweigart al@inventwithpython.com
    Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''')

    if ask_for_tutorial():
        run_tutorial()

    money = 5000
    while True:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        print('Money:', money)
        bet = get_bet(money)
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        print('Bet:', bet)

        if is_natural_blackjack(player_hand):
            display_hands(player_hand, dealer_hand, True)
            print('Natural blackjack! You win a 10-to-1 payout!')
            money += bet * 10
            input('Press Enter to continue...')
            print('\n\n')
            continue

        split_hands = []
        split_bets = []
        if can_split(player_hand) and money >= bet * 2:
            if ask_split_pair(player_hand):
                first_hand = [player_hand.pop(0)]
                second_hand = [player_hand.pop(0)]
                first_hand.append(deck.pop())
                second_hand.append(deck.pop())
                split_hands = [first_hand, second_hand]
                split_bets = [bet, bet]
                print('You split the pair into two hands.')
                print('Bet:', bet, 'on each hand.')
            else:
                split_hands = [player_hand]
                split_bets = [bet]
        else:
            split_hands = [player_hand]
            split_bets = [bet]

        for hand_index, (hand, hand_bet) in enumerate(zip(split_hands, split_bets), start=1):
            print(f'Hand {hand_index}')
            if not is_natural_blackjack(hand):
                while True:
                    display_hands(hand, dealer_hand, False)
                    print()

                    if get_hand_value(hand) > 21:
                        break

                    move = get_move(hand, money - hand_bet)

                    if move == 'D':
                        available_funds = money - hand_bet
                        additional_bet = get_bet(min(hand_bet, available_funds))
                        hand_bet += additional_bet
                        print('Bet increased to {}.'.format(hand_bet))
                        print('Bet:', hand_bet)

                    if move in ('H', 'D'):
                        new_card = deck.pop()
                        rank, suit = new_card
                        print('You drew a {} of {}.'.format(rank, suit))
                        hand.append(new_card)

                        if get_hand_value(hand) > 21:
                            continue

                    if move in ('S', 'D'):
                        break

                if get_hand_value(hand) <= 21:
                    while get_hand_value(dealer_hand) < 17:
                        print()
                        print('Dealer hits...')
                        dealer_hand.append(deck.pop())
                        display_hands(hand, dealer_hand, False)

                        if get_hand_value(dealer_hand) > 21:
                            break
                        input('Press Enter to continue...')
                else:
                    print()
                    print('You have busted!')

                display_hands(hand, dealer_hand, True)
                money = resolve_hand_outcome(hand, dealer_hand, hand_bet, money)

        input('Press Enter to continue...')
        print('\n\n')


def ask_for_tutorial():
    while True:
        choice = input('Would you like to see the tutorial? (Y/N): ').upper().strip()
        if choice in ('Y', 'N'):
            return choice == 'Y'
        print('Please enter Y or N.')


def run_tutorial():
    print('\n=== Blackjack Tutorial ===')
    print('1. Objective: try to get closer to 21 than the dealer without going over.')
    print('2. Card values: number cards are worth face value, face cards are worth 10, and Aces count as 1 or 11.')
    print('3. Dealer rule: the dealer must hit until reaching 17, then stand.')
    print('4. Your choices: (H)it takes a card; (S)tand keeps your hand as-is; (D)ouble down doubles your bet and takes one final card.')
    print('5. Split rule: if your first two cards have the same value, you may split them into two hands and bet on each separately.')
    print('6. Natural blackjack: an Ace of Spades plus any black jack (Spades or Clubs) in your first two cards pays 10-to-1.')
    print('7. Basic strategy: stand on 17 or more, hit on 11 or less, hit soft 17 or lower, and be cautious with pairs of 5s or 10s.')
    print('8. Good habit: watch the dealer up-card and avoid chasing losses. Playing conservatively often wins more often than risky guesses.')
    print('9. Common tip: if you have a pair of 8s or Aces, splitting is often the stronger move. If you have 10s or 5s, avoid splitting them.')
    print('10. After the tutorial, you will enter the main game with the same rules. Good luck!')
    input('\nPress Enter to continue...')
    print()


def card_value(rank):
    if rank == 'A':
        return 11
    if rank in ('K', 'Q', 'J'):
        return 10
    return int(rank)


def can_split(player_hand):
    if len(player_hand) != 2:
        return False
    return card_value(player_hand[0][0]) == card_value(player_hand[1][0])


def ask_split_pair(player_hand):
    if not can_split(player_hand):
        return False
    while True:
        choice = input('You have a pair. Split them? (Y/N): ').upper().strip()
        if choice in ('Y', 'N'):
            return choice == 'Y'
        print('Please enter Y or N.')


def is_natural_blackjack(cards):
    if len(cards) != 2:
        return False
    has_ace_spades = ('A', SPADES) in cards
    has_black_jack = any(card[0] in ('J', 'Q', 'K') and card[1] in (SPADES, CLUBS) for card in cards)
    return has_ace_spades and has_black_jack


def resolve_hand_outcome(player_hand, dealer_hand, bet, money):
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    if dealer_value > 21:
        print('Dealer busts! You win ${}!'.format(bet))
        return money + bet
    elif (player_value > 21) or (player_value < dealer_value):
        print('You lost!')
        return money - bet
    elif player_value > dealer_value:
        print('You won ${}!'.format(bet))
        return money + bet
    elif player_value == dealer_value:
        print("It's a tie, the bet is returned to you.")
        return money
    return money


def get_bet(max_bet):
    while True:
        print('How much do you bet? (1-{}) or QUIT'.format(max_bet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        display_cards([BACKSIDE] + dealer_hand[1:])

    print('PLAYER:', get_hand_value(player_hand))
    display_cards(player_hand)


def get_hand_value(cards):
    value = 0
    number_of_aces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces
    for _ in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    rows = ['', '', '', '', '']

    for card in cards:
        rows[0] += ' ___  '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def get_move(player_hand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


# Backward compatibility with the older naming used by the original file.
def getBet(maxBet):
    return get_bet(maxBet)


def getDeck():
    return get_deck()


def displayHands(playerHand, dealerHand, showDealerHand):
    display_hands(playerHand, dealerHand, showDealerHand)


def getHandValue(cards):
    return get_hand_value(cards)


def displayCards(cards):
    display_cards(cards)


def getMove(playerHand, money):
    return get_move(playerHand, money)


if __name__ == '__main__':
    main()
import datetime
import random

SIMULATIONS = 100_000


def parse_birthday(raw_value):
    """Return a date object from a user-entered birthday string."""
    value = raw_value.strip()
    formats = (
        '%m/%d/%Y',
        '%m-%d-%Y',
        '%m/%d/%y',
        '%m-%d-%y',
        '%Y/%m/%d',
        '%Y-%m-%d',
    )

    for fmt in formats:
        try:
            return datetime.datetime.strptime(value, fmt).date()
        except ValueError:
            continue

    raise ValueError(
        'Invalid birthday format. Please enter a date like MM/DD/YYYY or YYYY-MM-DD.'
    )


def generate_birthdays(number_of_birthdays):
    """Create a list of random birthdays for a group of people."""
    if number_of_birthdays < 1:
        raise ValueError('The group size must be at least 1 person.')

    birthdays = []
    for _ in range(number_of_birthdays):
        start_of_year = datetime.date(2001, 1, 1)
        random_days = datetime.timedelta(random.randint(0, 364))
        birthdays.append(start_of_year + random_days)
    return birthdays


def count_matching_birthdays(birthdays, target_birthday):
    """Count how many people in a group share the target birthday month and day."""
    return sum(
        1
        for birthday in birthdays
        if birthday.month == target_birthday.month and birthday.day == target_birthday.day
    )


def run_simulations(group_size, target_birthday, simulations=SIMULATIONS):
    """Run many groups and report how often any birthday matches the target."""
    groups_with_match = 0
    total_matches = 0

    for _ in range(simulations):
        birthdays = generate_birthdays(group_size)
        match_count = count_matching_birthdays(birthdays, target_birthday)
        total_matches += match_count
        if match_count > 0:
            groups_with_match += 1

    probability = (groups_with_match / simulations) * 100
    average_matches = total_matches / simulations
    return groups_with_match, average_matches, probability


def select_group_size():
    """Let the user choose a group size from a small menu or custom input."""
    options = {
        1: 20,
        2: 40,
        3: 60,
        4: 100,
    }

    print('\nChoose a group size:')
    print('  1) 20 people (small group)')
    print('  2) 40 people (normal class size)')
    print('  3) 60 people (larger class size)')
    print('  4) 100 people (large group)')
    print('  5) Enter your own size')

    while True:
        try:
            choice = input('Select an option (1-5): ').strip()
            option = int(choice)
        except ValueError:
            print('Please enter a number from 1 to 5.')
            continue

        if option in options:
            return options[option]

        if option == 5:
            while True:
                try:
                    custom_size = int(input('Enter a custom group size (1-200): ').strip())
                except ValueError:
                    print('Please enter a whole number between 1 and 200.')
                    continue

                if 1 <= custom_size <= 200:
                    return custom_size
                print('Group size must be between 1 and 200.')

        print('Please choose 1, 2, 3, 4, or 5.')


def format_birthday(date_obj):
    return date_obj.strftime('%b %d, %Y')


def run_analysis(user_birthday):
    group_size = select_group_size()

    print('\nGenerating one sample group with', group_size, 'people...')
    sample_group = generate_birthdays(group_size)
    sample_matches = count_matching_birthdays(sample_group, user_birthday)
    print(f'In this sample group, {sample_matches} person(s) share your birthday.')

    print(f'\nRunning {SIMULATIONS:,} simulations for groups of {group_size} people...')
    groups_with_match, average_matches, probability = run_simulations(
        group_size,
        user_birthday,
        SIMULATIONS,
    )

    print(f'Your birthday: {format_birthday(user_birthday)}')
    print(f'Group size: {group_size} people')
    print(f'Chance that at least one person matches your birthday: {probability:.2f}%')
    print(f'This happened in {groups_with_match:,} out of {SIMULATIONS:,} simulations.')
    print(f'Average number of matching birthdays per simulation: {average_matches:.2f}')
    print('That is why the birthday paradox feels so surprising!')


def main():
    print('Birthday Paradox Simulator')
    print('Adapted from Al Sweigart al@inventwithpython.com')
    print('This program estimates how often someone in a random group shares your birthday.')
    print('It compares the month and day only, not the year.')
    print()

    while True:
        while True:
            try:
                user_input = input('Enter your birthday (MM/DD/YYYY): ')
                user_birthday = parse_birthday(user_input)
                break
            except ValueError as exc:
                print(f'Invalid input: {exc}')
                print('Try again, for example: 03/15/1998 or 1998-03-15')
                print()

        run_analysis(user_birthday)

        while True:
            try:
                play_again = input('\nWould you like to run another simulation? (yes/no): ').strip().lower()
            except (EOFError, KeyboardInterrupt):
                print('\nGoodbye!')
                return

            if play_again in {'y', 'yes'}:
                print('\nGreat! Let\'s try another one.')
                break
            if play_again in {'n', 'no'}:
                print('\nThanks for playing!')
                return
            print('Please answer yes or no.')


if __name__ == '__main__':
    main()

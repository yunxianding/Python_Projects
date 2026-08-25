import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
CELL_WIDTH = 10
NOTES_PER_DAY = 3


def parse_positive_int(raw_text, field_name):
    value = int(raw_text)
    if value <= 0:
        raise ValueError(f'{field_name} must be greater than 0.')
    return value


def prompt_year():
    while True:
        print('Enter the year for the calendar:')
        response = input('> ').strip()
        try:
            return parse_positive_int(response, 'Year')
        except ValueError:
            print('Please enter a numeric year, like 2026.')


def prompt_month():
    while True:
        print('Enter the month for the calendar (1-12):')
        response = input('> ').strip()
        try:
            month = parse_positive_int(response, 'Month')
            if not 1 <= month <= 12:
                raise ValueError('Month must be from 1 to 12.')
            return month
        except ValueError:
            print('Please enter a number from 1 to 12.')


def last_day_of_month(year, month):
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    return (next_month - datetime.timedelta(days=1)).day


def prompt_special_days(year, month):
    special_days = {}
    max_day = last_day_of_month(year, month)

    print('How many special days do you want to add? (0 for none)')
    while True:
        response = input('> ').strip()
        try:
            count = int(response)
            if count < 0:
                raise ValueError('Count cannot be negative.')
            break
        except ValueError:
            print('Please enter 0 or a positive whole number.')

    for index in range(1, count + 1):
        print(f'Special day {index} of {count}')

        while True:
            print(f'Enter day number (1-{max_day}):')
            day_response = input('> ').strip()
            try:
                day = int(day_response)
                if not 1 <= day <= max_day:
                    raise ValueError('Day out of range for this month.')
                break
            except ValueError:
                print(f'Please enter a day between 1 and {max_day}.')

        while True:
            print('Enter note text within 10 characters(for example: Mom Btd):')
            note = input('> ').strip()
            if note:
                break
            print('Note text cannot be empty.')

        special_days.setdefault(day, []).append(note)

    return special_days


def get_calendar_for(year, month, special_days=None):
    if not isinstance(year, int) or year <= 0:
        raise ValueError('Year must be a positive integer.')
    if not isinstance(month, int) or not 1 <= month <= 12:
        raise ValueError('Month must be from 1 to 12.')

    special_days = special_days or {}
    month_last_day = last_day_of_month(year, month)
    for day in special_days:
        if not isinstance(day, int) or not 1 <= day <= month_last_day:
            raise ValueError(f'Special day {day} is outside this month.')

    cal_text = ''
    cal_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    cal_text += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    week_separator = ('+----------' * 7) + '+\n'
    month_end = datetime.date(year, month, month_last_day)
    current_date = datetime.date(year, month, 1)

    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        cal_text += week_separator

        week_dates = []
        day_number_row = ''
        for _ in range(7):
            week_dates.append(current_date)
            if current_date.month == month:
                day_number_label = str(current_date.day).rjust(2)
                day_number_row += '|' + (day_number_label + (' ' * 8))
            else:
                day_number_row += '|' + (' ' * CELL_WIDTH)
            current_date += datetime.timedelta(days=1)
        day_number_row += '|\n'
        cal_text += day_number_row

        for note_index in range(NOTES_PER_DAY):
            note_row = ''
            for date_value in week_dates:
                if date_value.month != month:
                    note_text = ''
                else:
                    notes = special_days.get(date_value.day, [])
                    note_text = notes[note_index] if note_index < len(notes) else ''
                note_row += '|' + note_text[:CELL_WIDTH].ljust(CELL_WIDTH)
            note_row += '|\n'
            cal_text += note_row

        if current_date > month_end and current_date.weekday() == 6:
            break

    cal_text += week_separator
    return cal_text


def save_calendar_to_file(cal_text, year, month):
    calendar_filename = f'calendar_{year}_{month}.txt'
    with open(calendar_filename, 'w', encoding='utf-8') as file_obj:
        file_obj.write(cal_text)
    return calendar_filename


def main():
    print('Calendar Maker, adapted from Al Sweigart al@inventwithpython.com')

    while True:
        try:
            year = prompt_year()
            month = prompt_month()
            special_days = prompt_special_days(year, month)
            cal_text = get_calendar_for(year, month, special_days)

            print(cal_text)
            saved_filename = save_calendar_to_file(cal_text, year, month)
            print('Saved to ' + saved_filename)
        except (ValueError, OSError) as exc:
            print(f'Error: {exc}')
        except KeyboardInterrupt:
            print('\nExiting Calendar Maker.')
            break

        print('Make another calendar? (y/n)')
        response = input('> ').strip().lower()
        if response not in ('y', 'yes'):
            print('Goodbye!')
            break


if __name__ == '__main__':
    main()
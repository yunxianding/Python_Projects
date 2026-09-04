import shutil

UP_DOWN_CHAR = '│'
LEFT_RIGHT_CHAR = '─'
DOWN_RIGHT_CHAR = '┌'
DOWN_LEFT_CHAR = '┐'
UP_RIGHT_CHAR = '└'
UP_LEFT_CHAR = '┘'
UP_DOWN_RIGHT_CHAR = '├'
UP_DOWN_LEFT_CHAR = '┤'
DOWN_LEFT_RIGHT_CHAR = '┬'
UP_LEFT_RIGHT_CHAR = '┴'
CROSS_CHAR = '┼'

OPPOSITE_DIRECTIONS = {'W': 'S', 'A': 'D', 'S': 'W', 'D': 'A'}
CELL_CHARS = {
    frozenset(('W', 'S')): UP_DOWN_CHAR,
    frozenset(('W',)): UP_DOWN_CHAR,
    frozenset(('S',)): UP_DOWN_CHAR,
    frozenset(('A', 'D')): LEFT_RIGHT_CHAR,
    frozenset(('A',)): LEFT_RIGHT_CHAR,
    frozenset(('D',)): LEFT_RIGHT_CHAR,
    frozenset(('S', 'D')): DOWN_RIGHT_CHAR,
    frozenset(('S', 'A')): DOWN_LEFT_CHAR,
    frozenset(('W', 'D')): UP_RIGHT_CHAR,
    frozenset(('W', 'A')): UP_LEFT_CHAR,
    frozenset(('W', 'S', 'D')): UP_DOWN_RIGHT_CHAR,
    frozenset(('W', 'S', 'A')): UP_DOWN_LEFT_CHAR,
    frozenset(('S', 'A', 'D')): DOWN_LEFT_RIGHT_CHAR,
    frozenset(('W', 'A', 'D')): UP_LEFT_RIGHT_CHAR,
    frozenset(('W', 'S', 'A', 'D')): CROSS_CHAR,
}


def get_canvas_size():
    """Return a usable canvas size even when terminal-size detection fails."""
    try:
        terminal_width, terminal_height = shutil.get_terminal_size()
    except OSError:
        terminal_width, terminal_height = 80, 25
    return max(1, terminal_width - 1), max(1, terminal_height - 5)


def get_canvas_string(canvas_data, cursor_x, cursor_y, width, height):
    """Return a multiline string showing the drawing and cursor."""
    canvas_lines = []
    for row in range(height):
        line = []
        for column in range(width):
            if column == cursor_x and row == cursor_y:
                line.append('#')
            else:
                cell = frozenset(canvas_data.get((column, row), ()))
                line.append(CELL_CHARS.get(cell, ' '))
        canvas_lines.append(''.join(line))
    return '\n'.join(canvas_lines) + '\n'


def move_cursor(canvas, cursor_x, cursor_y, direction, width, height):
    """Draw one line and return the cursor's new position."""
    offsets = {'W': (0, -1), 'A': (-1, 0), 'S': (0, 1), 'D': (1, 0)}
    offset_x, offset_y = offsets[direction]
    new_x = cursor_x + offset_x
    new_y = cursor_y + offset_y
    if not (0 <= new_x < width and 0 <= new_y < height):
        return cursor_x, cursor_y

    canvas.setdefault((cursor_x, cursor_y), set()).add(direction)
    canvas.setdefault((new_x, new_y), set()).add(OPPOSITE_DIRECTIONS[direction])
    return new_x, new_y


def save_drawing(filename, moves, canvas, width, height):
    """Save the command history and drawing to a text file."""
    filename = filename.strip()
    if not filename:
        raise ValueError('filename cannot be empty')
    if not filename.endswith('.txt'):
        filename += '.txt'
    with open(filename, 'w', encoding='utf-8') as drawing_file:
        drawing_file.write(''.join(moves) + '\n')
        drawing_file.write(get_canvas_string(canvas, None, None, width, height))
    return filename


def print_help():
    print('Enter W, A, S, and D to move the cursor and draw a line.')
    print('The cursor leaves a line behind it as it moves.')
    print('Use C to clear, F to save, or QUIT to exit.')


def main():
    width, height = get_canvas_size()
    canvas = {}
    moves = []
    cursor_x = 0
    cursor_y = 0

    try:
        while True:
            print(get_canvas_string(canvas, cursor_x, cursor_y, width, height))
            print('WASD keys to move, H for help, C to clear, F to save, or QUIT.')
            response = input('> ').strip().upper()

            if response == 'QUIT':
                print('Thanks for playing!')
                return
            if response == 'H':
                print_help()
                input('Press Enter to continue.')
                continue
            if response == 'C':
                canvas.clear()
                moves.append('C')
                continue
            if response == 'F':
                try:
                    filename = input('Enter a filename to save your drawing: ')
                    saved_filename = save_drawing(filename, moves, canvas, width, height)
                    print(f'Drawing saved to {saved_filename}.')
                except (EOFError, OSError, ValueError) as error:
                    print(f'Could not save drawing: {error}')
                continue

            for command in response:
                if command not in OPPOSITE_DIRECTIONS:
                    print(f'Invalid command: {command}. Use W, A, S, D, H, C, F, or QUIT.')
                    continue
                moves.append(command)
                cursor_x, cursor_y = move_cursor(
                    canvas, cursor_x, cursor_y, command, width, height
                )
    except (EOFError, KeyboardInterrupt):
        print('\nThanks for playing!')


if __name__ == '__main__':
    main()
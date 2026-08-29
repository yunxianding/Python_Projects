import argparse
import os
import random
import time

WIDTH = 79
HEIGHT = 20
ALIVE = '0'
DEAD = ' '


def random_board(width, height, live_percentage):
    """Return a board with a requested percentage of randomly live cells."""
    if not 0 <= live_percentage <= 100:
        raise ValueError('live percentage must be between 0 and 100')

    return {
        (x, y)
        for x in range(width)
        for y in range(height)
        if random.random() < live_percentage / 100
    }


def load_board(filename, width=WIDTH, height=HEIGHT):
    """Load live cells from a text file, using 0 for live and space for dead."""
    with open(filename, encoding='utf-8') as state_file:
        lines = state_file.read().splitlines()

    if len(lines) > height or any(len(line) > width for line in lines):
        raise ValueError(f'initial state must fit within {width}x{height}')

    board = set()
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell == ALIVE:
                board.add((x, y))
            elif cell not in (DEAD, '.'):
                raise ValueError("initial state may contain only '0', '.', or spaces")
    return board


def next_generation(board, width=WIDTH, height=HEIGHT):
    """Calculate a generation by counting neighbors around live cells only."""
    neighbor_counts = {}
    for x, y in board:
        for x_offset in (-1, 0, 1):
            for y_offset in (-1, 0, 1):
                if x_offset == 0 and y_offset == 0:
                    continue
                neighbor = ((x + x_offset) % width, (y + y_offset) % height)
                neighbor_counts[neighbor] = neighbor_counts.get(neighbor, 0) + 1

    return {
        cell for cell, count in neighbor_counts.items()
        if count == 3 or (count == 2 and cell in board)
    }


def display(board, width=WIDTH, height=HEIGHT):
    """Print a board to the terminal."""
    for y in range(height):
        for x in range(width):
            print(ALIVE if (x, y) in board else DEAD, end='')
        print()


def main():
    parser = argparse.ArgumentParser(description="Run Conway's Game of Life.")
    parser.add_argument(
        '--live-percentage', type=float, default=30,
        help='percentage of cells initially alive for a random board (default: 30)',
    )
    parser.add_argument(
        '--initial-state', metavar='FILE',
        help='text file containing the initial state; 0 means alive, space or . means dead',
    )
    parser.add_argument('--delay', type=float, default=1, help='seconds between generations')
    args = parser.parse_args()

    if args.delay < 0:
        parser.error('--delay cannot be negative')

    if args.initial_state:
        board = load_board(args.initial_state)
    else:
        board = random_board(WIDTH, HEIGHT, args.live_percentage)

    try:
        while True:
            os.system('clear')
            display(board)
            print("Press Ctrl-C to quit.")
            board = next_generation(board)
            time.sleep(args.delay)
    except KeyboardInterrupt:
        print('Conway\'s Game of Life')


if __name__ == '__main__':
    main()
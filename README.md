# Python Projects

This folder is a personal practice space for building small Python projects and games.

My goal is to improve my Python skills by working through short project ideas inspired by The Big Book of Small Python Projects and freeCodeCamp Python practice exercises. For each project, I try to add my own improvements and extensions beyond the original example.

## Daily Project Routine

I plan to add one small Python project or game to this folder each day. Each project will be focused on one learning goal and will include a short description, the rules, and any personal improvements I add beyond the original idea.

## Current Projects

Use this template for every new project in this folder:

### Project Name

- File: [ProjectName.py](ProjectName.py)
- Difficulty: Beginner / Intermediate / Advanced
- Skills practiced: loops, conditionals, functions, input handling, randomness, file I/O, etc.
- Description: A short explanation of what the project does.
- Rules: How the game or program works.
- My improvements: Extra features or refinements beyond the original example.
- Learning goal: What I wanted to practice while building it.

### Bagels

- File: [Bagels.py](Bagels.py)
- Difficulty: Beginner to Intermediate
- Skills practiced: loops, conditionals, functions, string handling, input validation, randomness, debugging
- Description: A guessing game where the player tries to determine a secret number using clue-based feedback.
- Rules:
  - The computer picks a secret number with no repeated digits.
  - The player attempts to guess the number.
  - The game responds with clues:
    - Fermi = correct digit in the correct position
    - Pico = correct digit in the wrong position
    - Bagels = no correct digits
  - The player wins by guessing the number before running out of attempts.
- My improvements:
  - stronger input validation
  - repeated-digit checks
  - clearer game flow
  - difficulty levels that increase the challenge
  - safer handling of invalid input and interruptions
- Learning goal: Practice control flow, validation, and building a small game with user interaction.

### Birthday Paradox

- File: [birthday_paradox.py](birthday_paradox.py)
- Difficulty: Beginner to Intermediate
- Skills practiced: loops, functions, user input handling, exception handling, randomness, simulation, probability
- Description: A Monte Carlo simulation game that estimates how likely people in a group are to share your birthday.
- Rules:
  - You enter your birthday.
  - The program lets you choose a group size (for example 20, 40, 60, 100, or a custom size).
  - It generates random birthdays for that group size many times.
  - It checks how often at least one person in each group shares your birthday (same month and day).
  - It shows the probability and average number of matches across all simulations.
- My improvements:
  - changed interaction to personalized input based on your birthday
  - added group-size menu options including class-size style presets
  - added play-again loop for repeated simulations
  - improved date-format validation and input error messages
  - improved output formatting for cleaner summaries
- Learning goal: Practice simulation thinking, probability intuition, input validation, and cleaner interactive program design.

### Blackjack

- File: [blackjack.py](blackjack.py)
- Difficulty: Beginner to Intermediate
- Skills practiced: loops, conditionals, functions, input handling, randomness, game logic, debugging
- Description: A command-line blackjack game where the player tries to beat the dealer by getting closer to 21 without busting.
- Rules:
  - The player starts with a bankroll and places a bet each round.
  - Number cards are worth face value, face cards are worth 10, and Aces can count as 1 or 11.
  - The dealer hits until reaching 17 and then stands.
  - The player can hit, stand, or double down on the first two cards.
  - If the first two cards match in value, the player may split them into two hands and play each separately.
  - A natural blackjack pays a 10-to-1 payout when the first two cards are an Ace of Spades and a black jack.
- My improvements:
  - added a beginner-friendly tutorial that can be skipped or viewed before the game starts
  - included clear rule explanations and basic strategy advice for new players
  - added split-hand support for matching pairs
  - added the natural blackjack payout rule
  - improved naming consistency and game flow for easier maintenance
- Learning goal: Practice game-state logic, card-hand evaluation, user prompts, and adding player-friendly rules to a classic game.

### Caesar Cipher

- File: [caesarcipher.py](caesarcipher.py) 
- Difficulty: Beginner
- Skills practiced: loops, conditionals, functions, input handling, strings, modulo arithmetic, exception handling
- Description: A command-line Caesar cipher tool that encrypts or decrypts text using a selected shift key.
- Rules:
  - The user chooses whether to encrypt or decrypt.
  - The user enters a key between 0 and the size of the symbol set.
  - Each character is shifted through the available alphabet.
  - Characters outside the allowed symbol set are left unchanged.
- My improvements:
  - expanded the symbol set to include uppercase letters, digits, punctuation, and spaces
  - fixed the mode-selection bug so encrypt and decrypt both work correctly
  - replaced the broad exception with a clearer clipboard error message
  - wrapped the script in a `main()` function for cleaner structure and easier testing
  - added safer handling for optional clipboard support when `pyperclip` is not installed
- Learning goal: Practice string manipulation, Caesar cipher logic, modular arithmetic, and writing cleaner interactive Python programs.

### Caesar Hacker

- File: [caesarhacker.py](caesarhacker.py)
- Difficulty: Beginner
- Skills practiced: loops, conditionals, functions, string handling, brute-force search, input handling, debugging
- Description: A command-line Caesar cipher hacker that brute-forces every possible shift and prints all candidate decryptions so you can spot the readable plaintext.
- Rules:
  - The user enters an encrypted message.
  - The program tries every possible key based on the symbol set.
  - Each key result is printed so the user can identify the correct plaintext.
  - The user can choose to hack another message in the same run.
- My improvements:
  - expanded the symbol set to include digits so mixed letter-number messages can be deciphered
  - preserved original letter case in decrypted output for better readability
  - added a main game loop with a play-again prompt
- Learning goal: Practice brute-force cryptanalysis, improve string transformation logic, and structure a small interactive program with reusable functions.

### Calendar Maker

- File: [calendarmaker.py](calendarmaker.py)
- Difficulty: Beginner to Intermediate
- Skills practiced: loops, conditionals, functions, input handling, exception handling, date handling, validation, file I/O
- Description: A command-line calendar generator that prints a monthly calendar and saves it to a text file, with optional special-day notes.
- Rules:
  - The user enters a valid year and month.
  - The program generates a month view aligned from Sunday to Saturday.
  - The user can add special-day notes by choosing a day number and entering short event text.
  - Notes are displayed inside each day cell and the calendar is saved as a `.txt` file.
  - The user can create another calendar in the same run.
- My improvements:
  - refactored the script into a `main()`-driven loop for repeated use
  - added stronger validation with targeted `ValueError` checks for year, month, and day ranges
  - added safer exception handling for user input, file writing errors, and `KeyboardInterrupt`
  - added special-day note support with per-day text entries
  - advised users to keep event names within 10 characters for better visual formatting
- Learning goal: Practice building a cleaner interactive CLI tool with robust validation, exception handling, and feature extensions on top of a date-based formatter.

### Cho-Han

- File: [chohan.py](chohan.py)
- Difficulty: Beginner to Intermediate
- Skills practiced: loops, functions, dictionaries, conditionals, input validation, randomness, and game-state management
- Description: A multiplayer command-line dice betting game based on the traditional Japanese game Cho-Han. The player competes against computer-controlled gamblers, each with an independent purse.
- Rules:
  - The player and computer gamblers begin with 5,000 mon each.
  - Each active gambler places one wager before two dice are rolled.
  - A Cho bet wins when the dice total is even; a Han bet wins when the total is odd.
  - Players may instead bet on an exact total from 2 through 12.
  - Correct Cho or Han bets pay 1x the wager as profit.
  - Correct exact-number bets pay 5x the wager as profit.
  - A total of 7 gives winning bets an additional 1x bonus.
  - Snake eyes, a total of 2, gives winning bets an additional 2x bonus.
  - A losing wager is removed from the gambler's purse.
  - The game continues until the player quits or runs out of mon. Computer gamblers with empty purses leave the game.
- My improvements:
  - added a main game loop with replay and quit options
  - added three computer-controlled gamblers with independent purses
  - added exact-number betting for totals from 2 through 12
  - added bonus payouts for lucky seven and snake eyes
  - added input validation for wagers and predictions
  - organized the game into reusable functions for bets, rounds, and payout settlement
- Learning goal: Practice decomposing an interactive game into functions while tracking multiple players, wagers, payouts, and changing game state.

### Conway's Game of Life

- File: [conwaysgameoflife.py](conwaysgameoflife.py)
- Difficulty: Intermediate
- Skills practiced: loops, functions, dictionaries, sets, randomness, file I/O, command-line arguments, and simulation logic
- Description: A terminal simulation of Conway's Game of Life, where cells evolve across generations according to their living neighbors.
- Rules:
  - A living cell survives when it has two or three living neighbors.
  - A dead cell becomes living when it has exactly three living neighbors.
  - All other cells become or remain dead.
  - The board wraps around at each edge, creating a continuous toroidal grid.
- My improvements:
  - added a main game loop with continuous generation updates
  - added a configurable random starting percentage with `--live-percentage`
  - added editable text-file starting states with `--initial-state`
  - added sparse neighbor counting that visits cells near living cells only
  - added command-line validation for board density and animation delay
- Learning goal: Practice simulation design, efficient state traversal, file input, and organizing a command-line program with reusable functions.
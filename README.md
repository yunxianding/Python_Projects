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

- File: [ceasarcipher.py](ceasarcipher.py)
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

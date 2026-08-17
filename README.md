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

# Project Statement. Number Guessing Game

## Problem Statement

beginners who are just starting out with programming find it hard to come up with simple fun projects that let them practice basic coding ideas. Things like loops if statements and handling errors can be tricky to understand at first. This project solves that problem by offering a interactive game where the user guesses a number. Its designed to be easy to follow and enjoy while helping learners get comfortable with core programming skills.

## Scope of the Project

This is a single-player game built in Python. It runs in the command line, no graphics, no interface—just text on screen. The focus is on keeping things simple and practical. Here’s what the game includes:

- A random number is picked each time between 1 and 100

- The user enters their guess through the keyboard

- The program checks if the input makes sense (like numbers

- After every guess it tells the player if their guess was too high or too low

- Once the user guesses correctly they can choose to play again without restarting the whole program

- Basic error handling so the game doesn’t crash if someone types letters instead of numbers

The game does **not** include:

- A graphical user interface (like buttons and windows)

- Support for more than one person playing at once

- Saving scores or remembering past wins

- Different difficulty levels or changing the range of numbers

- Making this into a website or phone app

## Target Users

- People who are just learning how to code and want to try something hands-on

- Students studying loops, conditions and how to handle mistakes in code

- Anyone who wants to play a quick guessing game using only the terminal

## High-Level Features

- **Random number generation:** Each round starts with a number chosen from 1, to 100 using Pythons `random` module

- **Interactive guessing loop:** The user keeps guessing until they get it right. The game keeps running until they succeed

- **Real-time hints:** After each guess the program says "too high" or "too low" to help guide the user

- **Input validation:** If the user tries to enter something that's n’t a number the program doesn’t break—it asks again politely

- **Replay capability:** After winning a round the user is asked if they want to play another game. No need to restart the application

- **readable codebase:** The code is written clearly so newcomers can read and learn from it easily

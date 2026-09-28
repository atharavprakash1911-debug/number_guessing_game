# Number Guessing Game 🎯

## Overview

This is a command-line game built in Python. Number Guessing Game picks a number between 1 and 100 and the player must guess it. After each guess Number Guessing Game gives a hint such as "please enter a number" or "please enter a smaller number" until the correct number is found. When a round ends Number Guessing Game asks the player for another game or to exit.

Number Guessing Game is a beginner- project built to practice core Python concepts such as nested loops, conditionals and exception handling.

## Features

- Randomly generates a number between 1 and 100 for each round.

- Provides real-time feedback such as "please enter a number" or "please enter a smaller number" after each guess.

- Checks user input and handles invalid entries such as letters or symbols without crashing.

- Allows the player to replay any number of rounds.

- Exits with a friendly closing message.

## Technologies / Tools Used

- **Language:** Python 3

- **Modules:** `(built-in Python module no external installation needed)

- **Environment:** Works in any terminal, IDE or code editor that supports Python, such as VS Code, PyCharm, IDLE, terminal or command prompt.

## Installation & Setup

### Prerequisites

- Python 3.x must be installed on your system. You can check by running:

```bash

python --version

```

```Bash

python3 --version

```

If it is not installed download it from [python.org](https://www.python.org/downloads/).

### Steps to run

1.. Clone the project files to your computer.

2. Open a terminal or command prompt. Go to the project folder:

```bash

cd path/to/project-folder

```

3. Run the script:

```bash

python number_guessing_game.py

```

(Use `python3` of `python` if you are on macOS/Linux and that is how Python 3 is set up on your machine.)

4. Follow the on-screen prompts to start playing.

## How to Play

1. When prompted type a number between 1 and 100.

2. Number Guessing Game will tell you if the guess is too high or too low.

3. Keep guessing until the correct number is found.

4. After a guess Number Guessing Game will ask for another game. Type `yes` to continue or anything else to quit.

## Testing Instructions

Since this is a console-based game testing is done manually by running the program and trying different scenarios. Here is what to check:

| Test Case | Input | Expected Result |

|---|---|---|

| Valid guess (correct) | The generated number | "Congratulation! your guess is message appears |

Valid guess (too low) | A number smaller than the target | "Please enter the number" message appears |

Valid guess (too high) | A number larger than the target | "Please enter the number" message appears |

| Invalid input | Letters, symbols or blank input | Program shows an error message. Asks again without crashing |

| Replay. Yes | Type `yes` after winning A new round starts with a new random number |

| Replay. No | Type `no` (or anything other than "yes”) | Program prints a thank‑you message. Exits |

To test it yourself:

1. Run the program.

2. Try entering numbers, out-of-range numbers and invalid text to confirm Number Guessing Game responds correctly each time.

3. Complete a round and test both the "yes" and "no" replay options.

## Screenshots

* the screen shot is attached below

```

enter your number betwwen 1 and 100: 50

Please enter the number

enter your number betwwen 1 and 100: 75

Please enter the smaller number

enter your number betwwen 1 and 100: 63

Congratulation! your guess is correct

Do you want to play ? (yes/no:) no

thanks, for playing the game

```

```

## License

I find this license simple and open: Free to use, modify and share for learning purposes.

```
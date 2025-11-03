# CS0 Final Lab - Game and Unit testing

Possible Points: 100

## Guess the Number game

The game generates a random number between 1 and 20 and asks the user to guess the number. The game provides hints to the user if the guess is too high or too low. The game ends when the user guesses the correct number or runs out of attempts. The players stats are stored in a YAML file.

## Lab Objectives

1. Learn about python packages and modules.
2. Learn about reading and writing YAML files.
3. Learn about using constants in Python.
4. Learn about using random module in Python.
5. Learn about using functions in Python.
6. Learn about refactoring and modular programming.
7. Learn about rich library for colorful output.

## Lab Setup

1. **tests** package contains the test files for the scripts.
2. **utility** package contains the utility/helper functions.
3. **settings.py** contains the game settings as constants.
4. **main.py** contains the main script to run the game.
5. **game.py** contains the game logic.

## Lab Instructions

1. Install **pyyaml**, **rich**, and **pytest** Python libraries required for the lab.

```bash
pip install pyyaml
pip install rich
pip install pytest
```

2. Learn about **rich** library here - [https://rich.readthedocs.io/en/stable/introduction.html](https://rich.readthedocs.io/en/stable/introduction.html) and **pyyaml** library here - [https://pyyaml.org/wiki/PyYAMLDocumentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

3. Run the lab script and understand what it does.

```bash
    $ python main.py
```

4. Use the partial implementation to complete **guessing_game** lab by fixing all the FIXMEs. (80 points)
   - see the packages **tests** and **utility** for the code to be fixed as well
5. Follow best programming practices by using proper white spaces, comments, etc.
6. Write Unittests for all the important fruitful functions and test using pytest.

```bash
    $ pytest -v tests/
```

7. Test the whole program manually.
8. Create screenshots showing your local test results (pytest and **manual test of all the game features**) and save them to the current lab folder. (20 points)
9. Update your README file (10 points with justification of self-grade) as shown here: [https://github.com/rambasnet/csxxx-rbasnet](https://github.com/rambasnet/csxxx-rbasnet)

## Submission

Add all the relevant source file(s), documents, and screenshots into the correct lab folder and do a final add, commit, and push before the due date.

```bash
$ git pull
$ git status
$ git add <filename>… - add each file in the red that is part of this lab
$ git status
$ git commit -m "Final Submission"
$ git push
$ git status
```

- Check and make sure the files are actually pushed to your GitHub repo.

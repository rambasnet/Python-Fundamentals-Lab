# CS0 Lab - Functions and Unittest

Possible Points: 100

Write a Python program to solve the Kattis problem: edays [https://open.kattis.com/problems/edays](https://open.kattis.com/problems/edays). Note that the last part of the URL, e.g. `edays` is the problem id. Read the problem statement carefully to design a correct solution.

## Kattis Setup

If not done before:

1. Create your account at [https://open.kattis.com](https://open.kattis.com). Change your university affiliation to Colorado Mesa University if you want to see your rank.
2. Setup kattis-cli for the Lab Codespace by clicking on and following [instructions here](https://coloradomesa365-my.sharepoint.com/:w:/g/personal/rbasnet_coloradomesa_edu/ESYiqurabGZJrIKmpCT4FnEBcw25QfcGjk_HK5PnRYbveA?e=xVLbe9)

## Download problem sample data and metadata

1. Change working directory to the current lab directory and execute the following Kattis command:

```bash
cd <lab directory>
kattis get edays
cd edays
kattis test
```

## Type and fix the code

1. Create an empty file named `edays.py` and `test_edays.py` in `edays` folder.
2. Type the contents provided in `edays.py` and `test_edays.py` files and fix all fixmes. Write #fixed# after each #fixme.
3. Follow best programming practices by using proper white spaces, comments, etc.

```txt
IMPORTANT: Never ask the user telling what data to enter for Kattis problems. Kattis knows what to enter.
Directly read the input. Print only the answer as displayed in the sample output.
Print as asked: nothing less; nothing more!
Kattis is a computer program that provides specific input and expects exact output – to a space to give the correct verdict.
```

## Whole program test with Kattis-cli

1. Test the whole program using Kattis-cli. While testing, provide input using the same format as described in the Input section and shown in input samples.
2. Add three new input and corresponding output files like the sample files inside data folder (10 points)
3. Test locally and submit to Kattis once all the tests pass

```bash
kattis test
kattis submit
```

## Unit testing with Pytest

1. Insall pytest library if required

```bash
pytest --version
pip install -U pytest
```

2. Run unit test using pytest and create screenshot when all the test cases pass. Install pytest if required. Pick one of the following ways to run pytest.

- Note that test modules must have prefix `test_` for pytest to find it.

```bash
cd <edays directory>
pytest --verbose
python -m pytest --verbose
```

## Submission

1. Create at least 3 screenshots showing your local tests (kattis test and pytest results) and the kattis final **Accept** verdict and save them to the **edays/screenshots** folder. (10 points).
2. Update the `README.md` file (10 points) as shown here: https://github.com/rambasnet/csXXX-rbasnet

```bash
git pull
git status
git add <each file in the red that is part of this lab>
git status
git commit -m "write brief description of what was done"
git push
git status
```

3. Make sure the files are actually pushed to your remote GitHub repo.

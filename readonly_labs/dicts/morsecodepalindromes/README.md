# CS0 Lab - Dictionary and Unit testing

Possible Points: 100

Write a Python program to solve the Kattis problem with id **morsecodepalindromes**: [https://open.kattis.com/problems/morsecodepalindromes](https://open.kattis.com/problems/morsecodepalindromes). Read the problem statement carefully to design a correct solution.

## Kattis Setup

If not done before:

1. Create your account at [https://open.kattis.com](https://open.kattis.com). Change your university affiliation to Colorado Mesa University if you want to see your rank.
2. Setup kattis-cli for the Lab Codespace by clicking on and following [instructions here](https://coloradomesa365-my.sharepoint.com/:w:/g/personal/rbasnet_coloradomesa_edu/ESYiqurabGZJrIKmpCT4FnEBcw25QfcGjk_HK5PnRYbveA?e=xVLbe9)

## Download problem sample data and metadata

1. Execute the following commands:

```bash
git pull
cd labs/dicts/
kattis get <problem id>
cd <problem id>
kattis test
```

2. Run the given partial solution to understand what it does.
3. Update all the Python files by fixing all the FIXMEs. Write #fixed# after each #FIXME.
4. Follow best programming practices by using proper white spaces, comments, etc.

```
IMPORTANT: Never ask the user telling what data to enter for Kattis problems. Kattis knows what to enter.
Directly read the input. Print only the answer as displayed in the sample output.
Print as asked: nothing less; nothing more!
Kattis is a computer program that provides specific input and expects exact output – to a space to give the correct verdict.
```

## Unit testing with Pytest

1. Insall pytest library if required

```bash
pytest --version
```

2. Run unit test using pytest and create screenshot when all the test cases pass. Install pytest if required. Pick one of the following ways to run pytest.

- Note that test modules must have prefix `test_` for pytest to find it.

```bash
cd <problem id>
pytest --verbose
```

## Whole program test with Kattis-cli

1. Test the whole program using Kattis-cli. While testing, provide input using the same format as described in the Input section and shown in input samples.
2. Add three new input and corresponding output files like the sample files inside data folder (10 points)
3. Test locally and submit to Kattis once all the tests pass

```bash
kattis test
kattis submit
```

## Submission

1. Create screenshots showing your local testings (kattis test and pytest results) and the kattis final **Accept** verdict and save them to the **screenshots** folder. (10 points)
2. Update your `labs/README.md` file (10 points) as shown here: <https://github.com/rambasnet/csci000-astudent>

```bash
cd /workspaces/<your git repo>
git pull
git status
git add <each file in the red that is part of this lab>
git status
git commit -m "Final submission of <problem id>"
git push
git status
```

3. Make sure the files are actually pushed to your remote GitHub repo.

# CS0 Lab - Conditionals and Unit testing - B

Possible Points: 100

Write a Python program to solve the Kattis problem with id **litagreining** [https://open.kattis.com/problems/litagreining](https://open.kattis.com/problems/litagreining). Read the problem statement carefully to design a correct solution. Note that the last part of the URL (litagreining) is the problem id.

## Kattis Setup

If not done before:

1. Create your account at [https://open.kattis.com](https://open.kattis.com). Change your university affiliation to Colorado Mesa University if you want to see your rank.
2. Setup kattis-cli for the Lab Codespace by clicking on and following [instructions here](https://coloradomesa365-my.sharepoint.com/:w:/g/personal/rbasnet_coloradomesa_edu/ESYiqurabGZJrIKmpCT4FnEBcw25QfcGjk_HK5PnRYbveA?e=xVLbe9)

## Download problem sample data and metadata

1. Execute the following commands:

```bash
cd /workspaces/<your git repo>
git pull
cd conditionals/
ls
kattis get <problem id>
ls
cd <problem id>
ls
```

2. Type the given partial solution and run as it is to learn what it does.
3. Fix all FIXMEs. Write #fixed# after each FIXME.
4. Run `kattis test` and `pytest -v` to see if the fixes are correct after each fix.
5. Follow best programming practices by using proper white spaces, comments, etc.

```
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
cd <problem id>
pytest --verbose
python -m pytest --verbose
```

## Submission

1. Create screenshots showing your local testings (kattis test and pytest results) and the kattis final **Accept** verdict and save them to the **thelastproblem/screenshots** folder. (10 points)
2. Update the `README.md` file (10 points) as shown here: https://github.com/rambasnet/CSXXX-rbasnet

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

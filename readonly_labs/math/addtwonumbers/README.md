# CS0 Lab - Math

Possible Points: 100

Write a Python program to solve the Kattis problem: addtwonumbers [https://open.kattis.com/problems/addtwonumbers](https://open.kattis.com/problems/addtwonumbers). Note that the last part of the URL, e.g. `addtwonumbers` is the problem id. Read the problem statement carefully to design a correct solution.

## Kattis Setup

If not done before:

1. Create your account at [https://open.kattis.com](https://open.kattis.com). Change your university affiliation to Colorado Mesa University if you want to see your rank.
2. Setup kattis-cli for the Lab Codespace by clicking on and following [instructions here](https://coloradomesa365-my.sharepoint.com/:w:/g/personal/rbasnet_coloradomesa_edu/ESYiqurabGZJrIKmpCT4FnEBcw25QfcGjk_HK5PnRYbveA?e=xVLbe9)

## Download problem sample data and metadata

1. Change working directory to `labs/math/` and execute the following Kattis command:

```bash
cd labs/math/
kattis get addtwonumbers
cd addtwonumbers
kattis test
```

2. Update `addtwonumbers.py` file and fix all fixmes. Write #fixed# after each #fixme.
3. Follow best programming practices by using proper white spaces, comments, etc.

```txt
- IMPORTANT: Never ask/prompt the user telling what to do for Kattis problems. Kattis knows what to enter. 
- Directly read the input. Print only the answer as displayed in the sample output. 
Print as asked: nothing less; nothing more!
- Kattis is a computer program that provides specific input and expects exact output – to a space to give the correct verdict.
```

## Whole program test with Kattis-CLI

1. Test the whole program manually. While testing, provide input using the same format as described in the Input section and shown in input samples.
2. Add three new input and corresponding output files like the sample files inside data folder (10 points)
3. Test locally and submit to Kattis once all the tests pass

```bash
kattis test
kattis submit
```

## Submission

1. Create screenshots showing your local testing and the kattis final Accept verdict and save them to the **addtwonumbers/screenshots** folder. (10 points)
2. Update your `labs/README.md` file (10 points) as shown here: https://github.com/rambasnet/csci000-astudent

```bash
git pull
git status
git add <each file in the red that is part of this lab>
git status
git commit -m "Final submission of <problem id>"
git push
git status
```

3. Make sure the files are actually pushed to your remote GitHub repo.

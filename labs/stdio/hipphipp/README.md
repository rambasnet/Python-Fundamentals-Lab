# CS0 - Variables and Standard Input/Output

## Lab B: Hipp Hipp

Read and solve the Kattis problem: https://open.kattis.com/problems/hipphipp

## Kattis-cli Setup

If not done before:

1. Create your account at [https://open.kattis.com](https://open.kattis.com). Change your university affiliation to Colorado Mesa University if you want to see your rank.
2. Setup kattis-cli for the Lab Codespace by clicking on and following [instructions here](https://coloradomesa365-my.sharepoint.com/:w:/g/personal/rbasnet_coloradomesa_edu/ESYiqurabGZJrIKmpCT4FnEBcw25QfcGjk_HK5PnRYbveA?e=xVLbe9)

## Download problem sample data and metadata

1. Change working directory to `stdio` and execute the following Kattis command:

```bash
cd stdio
kattis get hipphipp
cd hipphipp
```

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

### Lab Instructions

1. Type the partial code provided in hiphipp.py file as it is in the current lab folder
2. Run the script to make sure the code runs without any syntax error
3. Fix all the FIXMEs and write #fixed# at the end of each FIXME that’s fixed except at the end of your name and date.

## Submission

- Create a folder called **screenshots** in the current lab folder (10 points)
  - create a screenshot of local kattis test
  - create a screenshot of remote kattis submit acceptance verdict
- Update main README file (10 points) as shown here: https://github.com/rambasnet/csxxx-rbasnet
- All FIXMEs are worth equal points unless stated otherwise.
- Add all the relevant source file(s), documents, and screenshots into the correct lab folder and do a final add, commit, and push before the due date.

```bash
$ git pull
$ git status
$ git add <each file in the red that is part of this lab>
$ git status
$ git commit -m "Final Submission"
$ git push
$ git status
```

- Check and make sure the files are actually pushed to your remote GitHub repository.

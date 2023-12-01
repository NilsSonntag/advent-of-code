# Advent of Code

## Description

Solutions to the Advent of Code Puzzles

## Setup

### Setup venv

Setup venv in your parent directory of this project:
cd there and use

```ps
python -m venv venv
```

Afterwards run

```ps
venv\Scripts\activate
```

If that leaves you with a ExecutionPolicy Error run

```ps
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

When you want your default Policy (probably Restricted) back, just use

```ps
Set-ExecutionPolicy Default -Scope CurrentUser
```

If you don't get an error your command line should look like this:

```ps
(venv) PS <working_directory>
```

### Install requirements

Continue by installing [requirements](requirements.txt) with pip.

```ps
(venv) PS> python -m pip install <package-name>
```

### Setup AOCD

Then setup your session cookie: [Guide](https://github.com/wimglenn/advent-of-code-wim/issues/1)
You probably want to write it in the text file at `~/.config/aocd/token` instead of exporting it to an environment variable.

Now you can test it on the console/terminal by writing `py` to start the python console and then:

```python
>>> from aocd.models import Puzzle
>>> puzzle = Puzzle(year=2023, day=1)
# Personal input data. Your data will be different.
>>> puzzle.input_data[:20]
'dqfournine5four2jmlq'
```

If that works you are good to go :)

Other features (not used yet): [Github link](https://github.com/wimglenn/advent-of-code-data)

## Usage

WIP

Run `init_day.py` once per day. It should generate all necessary files and folders. Start by checking if the generated `example.txt` file contains all the input.

Adjust the tests: First you then need to adjust the name of the solution file in the import section of `test_xx.py` (TODO: automate this). Then put in the example solution for part 1 and the wanted parse output. Try if the tests fail and check thereby if they work.

Now start working on the solution, start with the parse and work yourself down in the template.

## Authors and acknowledgment
All members

## License
MIT oder so

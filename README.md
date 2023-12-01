# Advent of Code

## Description

Solutions to the Advent of Code Puzzles

## Setup

### Setup venv

Setup a python virtual environment (venv) in your parent directory of this project:

```ps
cd ..
python -m venv venv
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
(venv) PS>
```

When you are done with the puzzle of the day you can use 

```ps
(venv) PS> deactivate
```

to stop the virtual environment.

### Install requirements

Continue by installing [requirements](requirements.txt) with pip.

```ps
(venv) PS> python -m pip install <package-name>
```

## Usage

WIP

Then setup your session cookie: [Guide](https://github.com/wimglenn/advent-of-code-wim/issues/1)
You probably want to write it in the text file at `~/.config/aocd/token` instead of exporting it to an environment variable.

Now you can use it on the console/terminal by writing `py` to start the python console and then:

```python
>>> from aocd.models import Puzzle
>>> puzzle = Puzzle(year=2023, day=1)
# Personal input data. Your data will be different.
>>> puzzle.input_data[:20]
'dqfournine5four2jmlq'
```

Other features (not used yet): [Github link](https://github.com/wimglenn/advent-of-code-data)

## Authors and acknowledgment
All members

## License
MIT oder so

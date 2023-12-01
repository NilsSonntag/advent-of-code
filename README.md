# Advent of Code

## Description

Solutions to the Advent of Code Puzzles

## Setup

Using Windows: 

```ps
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.ps1
```

Using Linux(Ubuntu or other distro with apt): 

```sh
source setup.sh
```

## Usage

Activate the virtual-environment session by using `.\venv\Scripts\Activate.ps1` on Windows and `source venv/bin/activate` on Linux.

When you are done with the daily puzzle run `deactivate` to stop the virtual-environment.

(WIP)

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

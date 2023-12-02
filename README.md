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

You have to put in your sessionID at the end of the setup. Here is how to get it:

1. Open [your input](https://adventofcode.com/2023/day/1/input) in the browser of your choice.
2. Right click and choose "Inspect" then navigate to
    - Application on Chrome
    - Network on Safari
    - Storage on Firefox
3. Open Cookies and choose the adventofcode one. There should be one cookie with the name "session". You need to copy that one and paste it into the terminal with Ctrl+Shift+V.

That was it and you can test it on the console/terminal by writing `py` to start the python console and then:

```python
>>> from aocd.models import Puzzle
>>> puzzle = Puzzle(year=2023, day=1)
# Personal input data. Your data will be different.
>>> puzzle.input_data[:20]
'dqfournine5four2jmlq'
```

And now you are done and ready to solve the daily puzzles :)

## Usage

Activate the virtual-environment session by using `.\venv\Scripts\Activate.ps1` on Windows and `source venv/bin/activate` on Linux.
When you are done with the daily puzzle run `deactivate` to stop the virtual-environment.

Run `init_day.py` once per day. It should generate all necessary files and folders. Start by checking if the generated `example.txt` file contains all the input.
Adjust the tests: Put in the example solution for part 1 and the wanted parse output. Try if the tests fail and check thereby if they work.
Now start working on the solution, start with the parse and work yourself down in the template.

## Authors and acknowledgment
All members

## License
MIT oder so

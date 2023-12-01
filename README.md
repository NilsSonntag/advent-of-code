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
    - ... on Firefox (TODO: Jonathan)
3. Open Cookies and choose the adventofcode one. There should be one cookie with the name "session". You need to copy that one and paste it into the terminal with Ctrl+Shift+V.

And now you are done and ready to solve the daily puzzles :)

## Usage

Activate the virtual-environment session by using `.\venv\Scripts\Activate.ps1` on Windows and `source venv/bin/activate` on Linux.

When you are done with the daily puzzle run `deactivate` to stop the virtual-environment.

## Authors and acknowledgment
All members

## License
MIT oder so

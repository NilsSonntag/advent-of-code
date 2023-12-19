import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    puzzle_input = puzzle_input.split("\n\n")
    dict_commands = {}
    for line in puzzle_input[0].splitlines():
        line = line.split("{")
        key = line[0]
        rules = line[1].replace("}",'')
        rules = rules.split(",")
        dict_commands[key] = rules
    parts = []
    for line in puzzle_input[1].splitlines():
        for letter in ["{","}","=","x","m","a","s"]:
            line = line.replace(letter,"")
        line=line.split(",")
        line = [int(a) for a in line]
        parts.append(line)
    return (dict_commands, parts)

def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""

def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input and return the solutions for part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    try:
        puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
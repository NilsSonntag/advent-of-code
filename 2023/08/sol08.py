import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    lines = puzzle_input.splitlines()
    left_rights = lines[0].strip()
    transitions = {}
    lines.pop(0)
    lines.pop(0)
    for line in lines:
        left_part, right_part = line.split("=")
        left_part = left_part.strip()
        right_part = right_part.strip()
        right_part_elements = right_part[1:9].split(",")
        right_part_elements[1] = right_part_elements[1].strip()
        transitions[left_part] = (right_part_elements[0], right_part_elements[1])
    return (left_rights, transitions)

def part1(data) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    left_rights, transitions = data
    steps = 0
    index = 0
    position = "AAA"
    while position != "ZZZ":
        if left_rights[index] == "L":
            position = transitions[position][0]
        else:
            position = transitions[position][1]
        steps += 1
        if index == len(left_rights)-1:
            index = 0
        else:
            index += 1
    return steps

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
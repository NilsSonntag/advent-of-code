import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> list[str]:
    """Parse the puzzle input and return a data structure."""
    return puzzle_input.split(",")



def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    sum_of_results = 0
    for item in data:
        current_value = 0
        for letter in item:
            current_value += ord(letter)
            current_value *= 17
            current_value %= 256
        sum_of_results += current_value
    return sum_of_results


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
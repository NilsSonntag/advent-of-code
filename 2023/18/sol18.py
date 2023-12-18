import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> list[tuple[str, int, str]]:
    """Parse the puzzle input and return a data structure."""
    result = []
    lines = puzzle_input.splitlines()
    for line in lines:
        result.append(line.split(" "))
    for i in range(len(result)):
        result[i][0] = result[i][0].strip()
        result[i][1] = int(result[i][1])
        result[i][2] = result[i][2].strip().strip("(").strip(")")
    return result

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
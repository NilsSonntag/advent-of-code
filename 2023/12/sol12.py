import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    splitted_by_line = puzzle_input.splitlines()
    springs = []
    error_struct = []
    for split in splitted_by_line:
        half=split.split(" ")
        springs.append(half[0])
        error_struct.append(half[1].split(","))
    error_struct = [[int(i) for i in j] for j in error_struct]
    return springs, error_struct

def get_error_struct(springs: str) -> list[int]:
    """Return the error struct of the given springs."""
    error_struct = []
    broken_count = 0
    
    for spring in springs:
        if spring == "#":
            broken_count += 1
        elif broken_count > 0:
            error_struct.append(broken_count)
            broken_count = 0
    
    if broken_count > 0:    
        error_struct.append(broken_count)
    
    return error_struct

def part1(data: tuple[list[str], list[list[int]]]) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    springs, error_struct = data
    total = 0
    
    for spring_row, errors in zip(springs, error_struct):
        num_of_questions = spring_row.count("?")
        
        for i in range(2**num_of_questions):
            to_test = spring_row
            
            for j in range(num_of_questions):
                if i & (1 << j):
                    to_test = to_test.replace("?", "#", 1)
                else:
                    to_test = to_test.replace("?", ".", 1)
            
            if get_error_struct(to_test) == errors:
                total += 1
    
    return total

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
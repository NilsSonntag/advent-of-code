import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

NUMBER_OF_STEPS = 64

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    return puzzle_input.splitlines()

def find_start(data: Any) -> Tuple[int, int]:
    """Find the starting position of the player."""
    for row in data:
        for char in row:
            if char == 'S':
                return data.index(row), row.index(char)
            
def replace_string(row : str, position: int, new_letter : str)->str:
    """Replace a letter in a string at a given position."""
    return row[:position] + new_letter + row[position+1:]

def count_possible_positions(data: Any) -> int:
    """Count the number of possible positions."""
    count = 0
    for row in data:
        count += row.count('O')
    return count

def make_step(data: Any) -> Any:
    """Make a step in the game."""
    new_data = data.copy()
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "O":
                if x>0 and data[x-1][y] in ".O":
                    new_data[x-1] = replace_string(new_data[x-1], y, "X")
                if x<len(data) and data[x+1][y] in ".O":
                    new_data[x+1] = replace_string(new_data[x+1], y, "X")
                if y>0 and data[x][y-1] in ".O":
                    new_data[x] = replace_string(new_data[x], y-1, "X")
                if y<len(data[0]) and data[x][y+1] in ".O":
                    new_data[x] = replace_string(new_data[x], y+1, "X")
                #consider case where current position was already replaced by new O
                if new_data[x][y] == "O":
                    new_data[x] = replace_string(new_data[x], y, ".")
    for x, row in enumerate(new_data):
        for y, char in enumerate(row):
            if char == "X":
                new_data[x] = replace_string(new_data[x], y, "O")
    return new_data

def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    start = find_start(data)
    data[start[1]] = replace_string(data[start[1]], start[1], "O")
    for i in range(NUMBER_OF_STEPS):
        data = make_step(data)
    return count_possible_positions(data)

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    pass

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
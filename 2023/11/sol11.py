import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> list[str]:
    """Parse the puzzle input and return a list of strings."""
    return puzzle_input.splitlines()

def rows_to_columns(data: list[str]) -> list[str]:
    """Return the data structure with rows and columns swapped."""
    return ["".join(row) for row in zip(*data)]

def row_contains_only_points(row: str) -> bool:
    """Return True if the given row contains only points, False otherwise."""
    return (row.find("#") == -1)

def expand(data: list[str]) -> list[str]:
    """Expand the given data structure by inserting point rows under rows that contain only points."""
    result = data.copy()
    counter = 0
    for i in range(len(data)):
        row = data[i]
        if row_contains_only_points(row):
            counter += 1
            result.insert(i+counter, "." * len(row))
    return result

def find_galaxies(data: list[str]) -> list[Tuple[int, int]]:
    """Return a list of galaxies in the given data structure."""
    galaxies = []
    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
            if row[j] == "#":
                galaxies.append((i, j))
    return galaxies

def expand_the_universe(data: list[str]) -> list[str]:
    """Expand the universe by using expand() on rows and coloumns."""    
    data = expand(data)
    coloumns = rows_to_columns(data)
    coloumns = expand(coloumns)
    data = rows_to_columns(coloumns)
    
    return data

def distance_between_points(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    """Return the distance between the given points."""
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    expanded = expand_the_universe(data)
    galaxies = find_galaxies(expanded)
    
    sum_shortest_path = 0
    for galaxy in galaxies:
        for galaxy2 in galaxies:
            if galaxy == galaxy2:
                continue
            sum_shortest_path += distance_between_points(galaxy, galaxy2)
    return sum_shortest_path // 2

def part2(data: list[str]) -> int:
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
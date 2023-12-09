import pathlib
from typing import List, Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    lines = puzzle_input.splitlines()
    return [[int(element) for element in line.split()] for line in lines]

def toZeroLine(input: List[int]) -> List[List[int]]:
    all_zeros = False
    pyramid = [input]
    line_counter = 0
    
    while not all_zeros:
        all_zeros = True
        pyramid.append([])
        line_counter += 1
        
        for i in range(1, len(pyramid[line_counter-1])):
            pyramid[line_counter].append(pyramid[line_counter-1][i]-pyramid[line_counter-1][i-1])
            
        if sum(pyramid[line_counter]) != 0:
            all_zeros = False
            
    return pyramid

def extrapolate(input: List[List[int]]) -> List[List[int]]:
    input[-1].append(0)
    
    for line_counter in range(2, len(input)+1):
        line_counter *= -1
        input[line_counter].append(input[line_counter+1][-1]+input[line_counter][-1])
        
    return input

def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    sum_history_value = 0
    extrapolation_field = [[line] for line in data]
    
    for i in range(len(data)):
        extrapolation_field[i] = toZeroLine(extrapolation_field[i][0])
        extrapolation_field[i] = extrapolate(extrapolation_field[i])
        sum_history_value += extrapolation_field[i][0][-1]
    
    return sum_history_value

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
        puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
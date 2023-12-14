import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    return puzzle_input.splitlines()

def transpose(data) -> Any:
    """Transpose the data structure."""
    data = list(zip(*data))
    for index in range(len(data)):
        data[index] = "".join(data[index])
    return data

def move_stones_north(line: str) -> str:
    """Move the stones north."""
    cut_line=line.split("#")
    for i in range(len(cut_line)):
        num_stones = cut_line[i].count("O")
        cut_line[i] = ''.join(['O']*num_stones + ['.']*(len(cut_line[i])-num_stones))
    line = "#".join(cut_line)
    return line

def calculate_weight(line: str) -> int:
    """Calculate the weight of the stones."""
    weight=0
    for i in range(len(line)):
        if line[i] == "O":
            weight+=len(line)-i
    return weight

def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    transposed = transpose(data)
    weight=0
    for line in transposed:
        line=move_stones_north(line)
        weight+=calculate_weight(line)
    return weight

def turn_matrix_left(data: Any) -> Any:
    """Turn the matrix left."""
    #data_new = data.copy()
    data_new = ["" for i in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data)):
            #print(i,j, data[-(j+1)][i])
            data_new[i] += data[j][-(i+1)]
        #data_new[i] = data[-(i+1)][::-1]
    return data_new

def move_all_stones(data: Any) -> Any:
    """Move all stones."""
    data_new = data.copy()
    for i in range(len(data)):
        data_new[i] = move_stones_north(data[i])
    return data_new

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    start_position = data
    weight=0
    i=0
    found_cycle=False
    while i<1000000000 and not found_cycle:
        position_new = start_position
        for j in range(4):
            transposed=move_all_stones(transpose(position_new))
            position_new = transpose(transposed)
            print("Old: ",position_new)
            position_new = turn_matrix_left(position_new)
            print("New: ",position_new)
        if start_position == position_new:
            found_cycle=True
        else:
            start_position = position_new
        i+=1
        #print(start_position)
    for line in start_position:
        weight+=calculate_weight(line)
    return weight

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
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


def turn_matrix_right(data: Any) -> Any:
    """Turn the matrix right."""
    data_new = data.copy()
    data_new = transpose(data_new)
    for i in range(len(data_new)):
        data_new[i] = data_new[i][::-1]
    return data_new

def move_all_stones(data: Any) -> Any:
    """Move all stones."""
    data_new = data.copy()
    for i in range(len(data)):
        data_new[i] = move_stones_north(data[i])
    return data_new

def print_matrix(data: Any) -> None:
    """Print the matrix."""
    for line in data:
        print(line)

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    start_position = data
    weight=0
    i=0
    found_cycle=False
    cycle_length=0
    end_position = start_position
    list_of_positions=[]
    while i<1000000000 and not found_cycle:
        position_new = start_position
        for j in range(4):
            transposed=move_all_stones(transpose(position_new))
            position_new = transpose(transposed)
            position_new = turn_matrix_right(position_new)
        print("New:----------------------------------------------------------------------------------------------------")
        print_matrix(position_new)
        if position_new in list_of_positions:
            found_cycle=True
            cycle_length = len(list_of_positions)-list_of_positions.index(position_new)
            print("Found cycle at: ",i,"for cycle length: ",cycle_length)
        else:
            list_of_positions.append(position_new)
            start_position = position_new
        i+=1
    positions_till_end = (1000000000-i)%cycle_length
    print("Positions till end: ",positions_till_end)
    end_position = list_of_positions[-cycle_length+positions_till_end]
    for line in transpose(end_position):
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
        puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
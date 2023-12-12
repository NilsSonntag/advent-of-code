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

def unfold(data: tuple[list[str], list[list[int]]]) -> tuple[list[str], list[list[int]]]:
    """Unfold the given data structure."""
    springs, error_struct = data
    new_springs = []
    for spring in springs:
        new_springs.append('?'.join([spring,spring,spring,spring,spring]))
    new_error_struct = []
    for error in error_struct:
        new_error_struct.append(error*5) 
    return new_springs, new_error_struct

DP_TABLE = {}

def calc_possible_configs(springs, error_struct, operational, damaged, lenght_of_current) -> int:
    """Calculate the number of possible configurations."""
    position_key=(operational, damaged, lenght_of_current)
    if position_key in DP_TABLE:
        return DP_TABLE[position_key]
    if operational == len(springs):
        if damaged == len(error_struct) and lenght_of_current == 0:
            return 1
        elif damaged == len(error_struct)-1 and error_struct[damaged] == lenght_of_current:
            return 1
        else:
            return 0
    val=0
    for crackter in ".#":
        if springs[operational] == crackter or springs[operational] == "?":
            if crackter=='.' and lenght_of_current==0:
                val+=calc_possible_configs(springs, error_struct, operational+1, damaged,0)
            elif crackter=='.' and lenght_of_current>0 and damaged<len(error_struct) and lenght_of_current==error_struct[damaged]:
                val+=calc_possible_configs(springs, error_struct, operational+1, damaged+1,0)
            elif crackter=='#':
                val+=calc_possible_configs(springs, error_struct, operational+1, damaged,lenght_of_current+1)
    DP_TABLE[position_key]=val
    return val

def part2(data: tuple[list[str], list[list[int]]]) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    springs, error_struct = unfold(data)
    res =0
    for spring in springs:
        DP_TABLE.clear()
        res_new = calc_possible_configs(spring, error_struct[springs.index(spring)], 0, 0, 0)
        res+=res_new
        print(spring, error_struct[springs.index(spring)],res_new , res)
        return res


def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input and return the solutions for part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    try:
        puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
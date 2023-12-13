import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    list_of_all=[]
    list_of_curr_pattern=[]
    for line in puzzle_input.splitlines():
        if len(line)>0:
            list_of_curr_pattern.append(line)
        else:
            list_of_all.append(list_of_curr_pattern)
            list_of_curr_pattern=[]
    list_of_all.append(list_of_curr_pattern)
    return list_of_all

def find_mirror_line_horizontal(data) -> int:
    for i in range(0, len(data)-1):
        is_mirror = False
        for j in range(1, min(i+2, len(data)-i)):
            if data[i+1-j] != data[i+j]:
                is_mirror = False
                break
            is_mirror = True
        if is_mirror:
            return i+1
    return -1

def find_mirror_line(data) -> int:
    """Find the position at which the pattern is a mirror match, if the mirror line is horizontal
       the line index is returned with a factor of 100"""
    #check first for each row then for each column
    ans = 0
    ans = find_mirror_line_horizontal(data)
    if ans>0:
        return ans*100
    #transpose the data
    data = list(zip(*data))
    ans = find_mirror_line_horizontal(data)
    return ans

def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    ans=0
    for pattern in data:
        ans+=find_mirror_line(pattern)
    return ans

def smudge_match(a: str, b: str) -> bool:
    difference = sum(a[i] != b[i] for i in range(len(a)))
    if difference == 1:
        return True
    return False

def find_mirror_smudge_horizontal(data) -> int:
    for i in range(0, len(data)-1):
        is_mirror = False
        changes_due = 1
        for j in range(1, min(i+2, len(data)-i)):
            if data[i+1-j] != data[i+j]:
                is_mirror = False
                if changes_due > 0 and smudge_match(data[i+1-j], data[i+j]):
                        changes_due -= 1
                else:
                    break
            is_mirror = True
        if is_mirror and changes_due == 0:
            print(i+1)
            return i+1
    return -1

def find_mirror_smudge_line(data) -> int:
    #check first for each row then for each column
    ans = 0
    ans = find_mirror_smudge_horizontal(data)
    if ans>0:
        return ans*100
    #transpose the data
    data = list(zip(*data))
    for index in range(len(data)):
        data[index] = "".join(data[index])
    ans = find_mirror_smudge_horizontal(data)
    return ans

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    ans=0
    for pattern in data:
        ans+=find_mirror_smudge_line(pattern)
    return ans

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
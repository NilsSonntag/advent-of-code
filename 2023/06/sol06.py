import pathlib
import time
from typing import List, Tuple

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    lines = [line.split(":",1)[1] for line in lines]
    lines = [line.strip() for line in lines]
    lines = [[int(item) for item in line.split()] for line in lines]
    as_tuples = []
    for i in range(len(lines[0])):
        as_tuples.append((lines[0][i], lines[1][i]))
    return as_tuples

def part1(data):
    """Solve part 1."""
    res=1
    for i in range(len(data)):
        err_margin=0
        for j in range(data[i][0]):
            if reached_range(data[i][0],j) > data[i][1]:
                err_margin += 1
        res *= err_margin
    return res

def reached_range(time, holding_time):
    return (time-holding_time)*holding_time

def to_single_race(data: List[Tuple[int,int]])->Tuple[int,int]:
    time = "".join(str(item[0]) for item in data)
    distance = "".join(str(item[1]) for item in data)
    return (int(time), int(distance))

def part2(data_in):
    """Solve part 2."""
    res=1
    time, distance = to_single_race(data_in)
    err_margin=0
    for i in range(time):
        if reached_range(time,i) > distance:
            err_margin = i
            break
    for i in range(time):
        if reached_range(time,time-i) > distance:
            err_margin = time-err_margin-i+1
            break
    return err_margin

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)	
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    start = time.time()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
    print("And it took", time.time() - start, "seconds to solve.")
import pathlib
from math import gcd
from typing import Tuple, Any
from collections import deque
from itertools import cycle
import time

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    lines = puzzle_input.splitlines()
    left_rights = lines[0].strip()
    transitions = {}
    lines.pop(0)
    lines.pop(0)
    for line in lines:
        left_part, right_part = line.split("=")
        left_part = left_part.strip()
        right_part = right_part.strip()
        right_part_elements = right_part[1:9].split(",")
        right_part_elements[1] = right_part_elements[1].strip()
        transitions[left_part] = (right_part_elements[0], right_part_elements[1])
    return (left_rights, transitions)

def part1(data) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    left_rights, transitions = data
    steps = 0
    index = 0
    position = "AAA"
    while position != "ZZZ":
        if left_rights[index] == "L":
            position = transitions[position][0]
        else:
            position = transitions[position][1]
        steps += 1
        if index == len(left_rights)-1:
            index = 0
        else:
            index += 1
    return steps

def nodes_ending_on_A (transitions: Any) -> list:
    """Return a list of nodes that end on A."""
    nodes_ending_on_A = []
    for node in transitions.keys():
        if node[2] == "A":
            nodes_ending_on_A.append(node)
    return nodes_ending_on_A

def part2 (data: Any) -> int:
    left_rights, transitions = data
    steps = 0
    positions = nodes_ending_on_A(transitions)
    cycles = []
    lr = left_rights
    for pos in positions:
        cycle = []
        steps = 0
        first_found = None
        while True:
            while steps == 0 or not pos.endswith("Z"):
                steps += 1
                pos = transitions[pos][0 if lr[0] == "L" else 1]
                lr = lr[1:] + lr [0]
            cycle.append(steps)
            if first_found is None:
                first_found = pos
                
            elif pos == first_found:
                break
        cycles.append(cycle)
        
    numbers = [cycle[0] for cycle in cycles]
    return lcm(numbers)
    
def lcm(numbers):
    res = numbers.pop() 
    for num in numbers:
        res  = res * num // gcd(res, num)
    return res

    

    
def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input and return the solutions for part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    start=time.time()
    solution2 = part2(data)
    print("Time: " + str(time.time()-start))

    return solution1, solution2

if __name__ == "__main__":
    try:
        puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
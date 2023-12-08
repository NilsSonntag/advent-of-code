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
"""
def part2(data: Any) -> int:
    left_rights, transitions = data
    steps = 0
    left_rights = deque(left_rights)
    positions = set(nodes_ending_on_A(transitions))
    found = False
    while not found:
        found = True
        lr = left_rights[0]
        updated_positions = set()
        for position in positions:
            updated_position = transitions[position][0] if lr == "L" else transitions[position][1]
            if updated_position[2] != "Z":
                found = False
                updated_positions.add(updated_position)
        if not found and steps > len(left_rights):
            mu, lam = find_cycle(position, cycle(left_rights), transitions)
            if lam != 0:
                cycle_repeats = (len(left_rights) - mu) // lam
                steps += cycle_repeats * lam
                left_rights.rotate(cycle_repeats * lam)
        else:
            steps += 1
            left_rights.rotate(1)
        positions = updated_positions
    return steps

def part2(data: Any) -> int:
    left_rights, transitions = data
    steps = 0
    left_rights = deque(left_rights)
    positions = set(nodes_ending_on_A(transitions))
    found = False
    while not found:
        found = True
        lr = left_rights[0]
        updated_positions = set()
        for position in positions:
            if lr == "L":
                updated_position = transitions[position][0]
            else:
                updated_position = transitions[position][1]
            if updated_position[2] != "Z":
                found = False
            updated_positions.add(updated_position)
        steps += 1
        left_rights.rotate(1)
        positions = updated_positions
    return steps

def find_cycle(position, left_rights, transitions):
    # Define a helper function that applies the transition
    def f(x):
        direction = next(left_rights)
        return transitions[x][0 if direction == "L" else 1]

    # Phase 1: Find a repetition x_mu = x_2mu.
    tortoise = f(position)
    hare = f(f(position))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Phase 2: Find the position of the first repetition of length lambda.
    mu = 0
    hare = position
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    # Phase 3: Find the length of the shortest cycle starting from x_mu.
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1

    return mu, lam
"""


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
    solution1 = 0
    #solution1 = part1(data)
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
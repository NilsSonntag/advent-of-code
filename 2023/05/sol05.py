import pathlib
import math
import time
from typing import List, Tuple

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse_seeds(puzzle_input_seeds: str) -> List[int]:
    """Parse seeds."""
    return list(map(int, puzzle_input_seeds.split(":", 1)[1].strip().split()))

def parse_rest(puzzle_input_rest: List[str]) -> List[List[List[int]]]:
    """Parse rest."""
    return [[[int(num) for num in line.strip().split()] for line in part.split(":", 1)[1].strip().splitlines()] for part in puzzle_input_rest]

def parse(puzzle_input: str) -> List[List[int]]:
    """Parse input."""
    parts = puzzle_input.split("\n\n")
    return [parse_seeds(parts[0])] + parse_rest(parts[1:])

def part1(data: List[List[int]]) -> int:
    seeds = data[0]
    minimum = math.inf

    for seed in seeds:
        current_value = seed

        for mapping in data[1:]:
            for destination_start, source_start, range_length in mapping:
                if source_start <= current_value < source_start + range_length:
                    current_value = destination_start + (current_value - source_start)
                    break

        minimum = min(minimum, current_value)

    return minimum


def compute_mapping(seed: Tuple[int, int], mapping: Tuple[int, int, int]) -> Tuple[List[Tuple[int, int]], Tuple[int, int]]:
    seed_start, seed_range = seed
    destination_start, source_start, range_length = mapping

    intersection_start = max(seed_start, source_start)
    intersection_end = min(seed_start + seed_range, source_start + range_length)

    current_list_addition = []
    next_list_addition = None

    if intersection_start < intersection_end:
        intersection_range = intersection_end - intersection_start
        next_list_addition = (destination_start + (intersection_start - source_start), intersection_range)

        if seed_start < intersection_start:
            current_list_addition.append((seed_start, intersection_start - seed_start))

        if seed_start + seed_range > intersection_end:
            current_list_addition.append((intersection_end, seed_start + seed_range - intersection_end))

    return current_list_addition, next_list_addition

def part2(data: List[List[int]]) -> int:
    """Solve part 2."""
    seeds_initial = data[0]
    next_list = [(seeds_initial[i],seeds_initial[i+1]) for i in range(0, len(seeds_initial), 2)]    

    for mapping_list in data[1:]:
        current_list = next_list 
        next_list = []

        for seed_tuple in current_list:
            changed = False
            
            for elem in mapping_list:
                current_list_additions, next_list_addition = compute_mapping(seed_tuple, elem)
                
                if current_list_additions:
                    current_list.extend(current_list_addition)
                    changed = True
                
                if next_list_addition is not None:
                    next_list.append(next_list_addition)
                    changed = True
                    
                if changed:
                    break
                
            if not changed:
                next_list.append(seed_tuple)
    
    return min(current_value[0] for current_value in next_list)



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    start= time.time()
    solution2 = part2(data)
    print("Time:" + str(time.time()-start))

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
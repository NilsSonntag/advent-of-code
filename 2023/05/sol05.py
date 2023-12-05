import pathlib
import math
import time

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse_seeds(puzzle_input_seeds):
    """Parse seeds."""
    seeds_string = puzzle_input_seeds.split(":",1)[1]
    seeds_numbers = [int(elem) for elem in seeds_string.strip().split()]
    return seeds_numbers

def parse_rest(puzzle_input_rest):
    """Parse rest."""
    parsed = []
    for part in puzzle_input_rest:  
        only_numbers = part.split(":",1)[1].strip().splitlines()
        parsed.append([[int(elem) for elem in line.strip().split()] for line in only_numbers])
    return parsed

def parse(puzzle_input):
    """Parse input."""
    # split the input to get all the parts
    parts = puzzle_input.split("\n\n")
    
    seeds_numbers = parse_seeds(parts[0])
    
    rest_parts = parse_rest(parts[1:])
    
    return [seeds_numbers] + rest_parts

def part1(data):
    """Solve part 1."""
    seeds = data[0]
    minimum = math.inf
    for seed in seeds:
        current_value = seed
        for i in range(1, len(data)):
            for elem in data[i]:
                destination_start = elem[0]
                source_start = elem[1]
                range_length = elem[2]
                if source_start <= current_value < source_start + range_length:
                    diff = current_value - source_start
                    current_value = destination_start + diff
                    break
        if current_value < minimum:
            minimum = current_value
    return minimum

def compute_mapping(seed_tuple, mapping):
    seed_start, seed_range = seed_tuple
    destination_start, source_start, range_length = mapping
    
    start_value = seed_start
    range_size = seed_range
    
    current_list_addition = []
    next_list_addition = None
    
    # case that the first values are not inside, but some of the other values are inside mapping
    if source_start > seed_start and source_start <= seed_start + seed_range:
        start_value = source_start
        range_size = seed_range - (start_value - seed_start)
        # add a new subrange that is before the mapping
        current_list_addition.append((seed_start, seed_range - range_size - 1))

    # case with first value in mapping independent of the rest
    if source_start <= start_value < source_start + range_length:
        diff = start_value - source_start
        diffgreater = start_value + range_size - source_start - range_length
        next_list_addition = (destination_start + diff, range_size - max(0, diffgreater))

        # some values are greater than the upper bound
        if diffgreater > 0:
            current_list_addition.append((seed_start+diffgreater, range_size - diffgreater))
    
    return current_list_addition, next_list_addition

def part2(data):
    """Solve part 2."""
    seeds_initial = data[0]
    minimum = math.inf
    next_list = [(seeds_initial[i],seeds_initial[i+1]) for i in range(0, len(seeds_initial), 2)]    

    for i in range(1, len(data)):
        current_list = next_list 
        next_list = []

        for seed_tuple in current_list:
            changed = False
            for elem in data[i]:
                current_list_additions, next_list_addition = compute_mapping(seed_tuple, elem)
                if current_list_additions != []:
                    for list_addition  in current_list_additions:
                        current_list.append(list_addition)
                    changed = True
                if next_list_addition is not None:
                    next_list.append(next_list_addition)
                    changed = True
                if changed:
                    break
            if not changed:
                next_list.append(seed_tuple)
    
    # compute minimum
    minimum = min([current_value[0] for current_value in next_list])
    return minimum



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
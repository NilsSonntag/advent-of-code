import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    """Parse input."""
    res = []
    parts = puzzle_input.split("\n\n")
    seeds_string = parts[0].split(":")[-1]
    seeds_numbers = [int(elem) for elem in seeds_string.strip().split()]
    res = [seeds_numbers]
    for part in parts[1:]:
        part_string = part.split(":")[-1].strip()
        part_numbers = [[int(elem) for elem in line.strip().split()] for line in part_string.splitlines()]
        res.append(part_numbers)
    return res

def part1(data):
    """Solve part 1."""
    seeds = data[0]
    minimum = -1
    for seed in seeds:
        currentValue = seed
        # print(currentValue)
        for i in range(1, len(data)):
            for elem in data[i]:
                if elem[1] <= currentValue < elem[1] + elem[2]:
                    diff = currentValue - elem[1]
                    currentValue = elem[0] + diff
                    # print(currentValue)
                    break
        if minimum == -1 or currentValue < minimum:
            minimum = currentValue
    return minimum

def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
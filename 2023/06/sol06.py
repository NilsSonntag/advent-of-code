import pathlib

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
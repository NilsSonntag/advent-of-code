import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    dict = {}
    for x in range(len(lines)):
        dict[x+1] = lines[x][(lines[x].find(":")+2):]
    return dict
        

def part1(data):
    """Solve part 1."""
    sum_id=0
    for x in range(len(data)+1):
        if x == 0: continue
        line = data[x].replace(",", ";")
        lineN = line.split(";")
        values = {"red": 0, "green": 0, "blue": 0}
        for element in lineN:
            element = element.strip()
            if element.find("red") != -1:
                values["red"] = max(int(element.split(" ")[0]), values["red"])
            elif element.find("green") != -1:
                values["green"] = max(int(element.split(" ")[0]), values["green"])
            elif element.find("blue") != -1:
                values["blue"] = max(int(element.split(" ")[0]), values["blue"])
        if values["red"] <= RED_MAX and values["green"] <= GREEN_MAX and values["blue"] <= BLUE_MAX:
            sum_id += x
    return sum_id

        


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
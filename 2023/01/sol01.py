import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.splitlines()
    return lines

def part1(data):
    """Solve part 1."""
    sum = 0
    for line in data:
        for element in line:
            if element.isdigit():
                sum += int(element) * 10
                break
        line = line [::-1]
        for element in line:
            if element.isdigit():
                sum += int(element)
                break
    return sum

def part2(data):
    """Solve part 2."""
    res = []
    for line in data:
        numbers = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
        for number in numbers:
            while(line.find(number) != -1):
                line = line [:line.find(number)+1] + numbers[number] + line [line.find(number)+1:]
        res.append(line)
    return part1(res)

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
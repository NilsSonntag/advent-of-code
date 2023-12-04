import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    """Parse input."""
    right_part=[]
    left_part=[]
    for lines in puzzle_input.splitlines():
        lines =lines.split(":",1)[-1]
        left = lines.split("|",1)[0]
        left = left.strip()
        left = [int(elem) for elem in left.split()]
        right = lines.split("|",1)[-1]
        right = right.strip()
        right = [int(elem) for elem in right.split()]
        left_part.append(left)
        right_part.append(right)
    return (left_part, right_part)

def part1(data):
    """Solve part 1."""
    solution = 0
    left_part = data[0]
    right_part = data[1]
    for i in range(len(left_part)):
        number = 0
        for elem in left_part[i]:
            if elem in right_part[i]:
                if number == 0:
                    number += 1
                else:
                    number *= 2
        solution += number
    return solution
         

def part2(data):
    """Solve part 2."""
    left_part = data[0]
    right_part = data[1]
    scratches = [1]*len(left_part)
    for i in range(len(left_part)):
        number = 0
        for elem in left_part[i]:
            if elem in right_part[i]:
                number += 1
        for j in range(number):
            if i + j + 1 < len(left_part):
                scratches[i+j+1] += scratches[i]
    return sum(scratches)

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
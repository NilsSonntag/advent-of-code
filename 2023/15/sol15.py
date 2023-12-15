import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> list[str]:
    """Parse the puzzle input and return a data structure."""
    return puzzle_input.split(",")

def hash_algorithm(data: str) -> int:
    """Hash algorithm for the given data."""
    current_value = 0
    for letter in data:
        current_value += ord(letter)
        current_value *= 17
        current_value %= 256
    return current_value

def part1(data: list[str]) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    sum_of_results = 0
    for item in data:
        sum_of_results += hash_algorithm(item)
    return sum_of_results

def split_string(string: str) -> list[str]:
    """Split the given string into a list of strings. Seperated by the caracter '-' or '='"""
    return string.split("-") if "-" in string else string.split("=")

def part2(data: list[str]) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    boxes = {}
    for i in range(256):
        boxes[i] = []
    
    for lens in data:
        lens = split_string(lens)
        label = lens[0]
        box_index = hash_algorithm(label)
        
        label_index = None
        for i in range(len(boxes[box_index])):
            if label in boxes[box_index][i]:
                label_index = i
                break
        
        if lens[1] is not "":
            is_contained = False
            for lenses in boxes[box_index]:
                if label == lenses[0]:
                    boxes[box_index][label_index] = lens
                    is_contained = True
                    break
            if not is_contained:
                boxes[box_index].append(lens)
        elif label_index is not None:
            del boxes[box_index][label_index]
    
    print(boxes)
    
    sum_of_powers=0
    for box in boxes:
        index_of_box = box + 1
        for lens in boxes[box]:
            index_of_slot = boxes[box].index(lens) + 1
            focal_length = int(boxes[box][index_of_slot - 1][1])
            sum_of_powers += focal_length * index_of_box * index_of_slot
    
    return sum_of_powers


def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input and return the solutions for part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    try:
        puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
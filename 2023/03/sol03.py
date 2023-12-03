import pathlib
import numpy as np
import string


PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    """Parse input."""
    all_punctuation = string.punctuation
    all_punctuation = all_punctuation.replace(".","#")
    for char in all_punctuation:
        puzzle_input = puzzle_input.replace(char, "#")
    width = len(puzzle_input.splitlines()[-1])
    height = len(puzzle_input.splitlines())
    puzzle_input = puzzle_input.replace("\n", "")
    return string_to_field(puzzle_input, width, height)

def filter (data):
    result =[]
    field = np.pad(data, 1, mode='constant', constant_values='.')
    for i in range(len(data)):
        j = 0
        while j < len(data[0]):
            if np.char.isdigit(data[i,j]):
                len_number = 1
                while(str(field[i+1, j+len_number+1]).isdigit()):
                    len_number += 1
                if '#' in field[i:i+3, j:j+len_number+2]:
                    whole_number = ""
                    for k in range(len_number):
                        whole_number = whole_number + data[i,j+k]
                    result.append(int(whole_number))
                j += len_number
            j += 1
    return result              

def part1(data):
    """Solve part 1."""
    return sum(filter(data))
    


def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


#This file contains various functions that provide functionalities useable in the event tasks

##Functions for input formatting--------------------------------------------------------------
#

def string_to_field(string_in, height, width, index_first=0, index_last=None):
    if not index_last: index_last=len(string_in)
    text=string_in[index_first:index_last].ljust(height*width, '0')
    arr=np.asarray([char for char in text])
    return arr.reshape(height,width)


#---------------------------------------------------------------------------------------------


if __name__ == "__main__":
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
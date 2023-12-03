import pathlib
import numpy as np
import string


PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input):
    """Parse input."""
    all_punctuation = string.punctuation
    all_punctuation = all_punctuation.replace(".","#")
    all_punctuation = all_punctuation.replace("*","#")
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
                if '#' in field[i:i+3, j:j+len_number+2] or '*' in field[i:i+3, j:j+len_number+2]:
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
    

def filter2(data):
    arr_of_numbers=np.zeros((len(data),len(data[0])), int)
    for i in range(len(data)):
        j = 0
        while j < len(data[0]):
            if np.char.isdigit(data[i,j]):
                number = int(data[i,j])
                len_number=1
                while(np.char.isdigit(data[i, j+len_number])):
                    number=number*10+int(data[i,j+len_number])
                    len_number+=1
                arr_of_numbers[i,j:j+len_number]=number
                j+=len_number
            j+=1
    return arr_of_numbers

"""
def part2(data):
    Solve part 2.
    whole_number_array = filter2(data)
    field = np.pad(data, 1, mode='constant', constant_values='.').tolist()
    test = np.zeros((len(field), len(field[0]))).tolist()
    test = test.tolist()
    for i in range(len(data)):
        j = 0
        for j in range(len(data[0])):
            if data[i,j] == '*':
                test[i][j] = 3.3
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if np.char.isdigit(field[x,y]):
                            test[x][y] = 5.5
    
    print(field.tolist())"""

def part2(data):
    """Solve part 2."""
    result = 0
    arr_of_numbers= filter2(data)
    field = np.pad(arr_of_numbers, 1, mode='constant', constant_values=0)
    for i in range(len(data)):
        j = 0
        while j < len(data[0]):
            if data[i,j]=='*':
                elem=np.unique(field[i:i+3,j:j+3])
                remova=np.argwhere(elem==0)
                elem2 = np.delete(elem, remova).tolist()
                print(elem2)
                if len(elem2)==2:
                    result += elem2[0]*elem2[1]
            j += 1
    return result 

    """
    result = 0
    gear_storage = {}
    field = np.pad(data, 1, mode='constant', constant_values='.')
    for i in range(len(data)):
        j = 0
        while j < len(data[0]):
            if np.char.isdigit(data[i,j]):
                len_number = 1
                while(str(field[i+1, j+len_number+1]).isdigit()):
                    len_number += 1
                if '*' in field[i:i+3, j:j+len_number+2]:
                    whole_number = ""
                    for k in range(len_number):
                        whole_number = whole_number + data[i,j+k]
                    indices = np.where(field[i:i+3, j:j+len_number+2] == '*')
                    print(indices)
                    gear_storage[indices].append(whole_number)
                    if(gear_storage > 0):
                        result += gear_storage * whole_number
                        gear_storage = 0
                    else:
                        gear_storage = whole_number
                j += len_number
            j += 1
    return result              
    """

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
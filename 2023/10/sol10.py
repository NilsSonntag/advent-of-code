import pathlib
from typing import Tuple, Any
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    lines = puzzle_input.splitlines()
    return lines

def get_start_position(data: Any) -> Tuple[int, int]:
    """Return the starting position of the animal."""
    for line in data:
        if not line.find("S")==-1:
            return (line.index("S"), data.index(line))
    return (-1, -1)

def rek_breadth_first_search_for_pipeloop(current_position: Tuple[int, int], data: Any, visited: Any) -> Tuple[int, int]:
    """Return the position where we first find a loop from start to start"""
    stack=[]
    while current_position not in visited:
        visited.append(current_position)
        
        x,y = current_position[0],current_position[1]
        print(x,y)

        #find all fitting neighbours
        adders = neighbours_to_add(current_position,data)
        print(adders)

        #for all the found fitting neighbours, add them to the stack
        for i in range(0,3):
            if adders[i]:
                if i==0:
                    stack.append((x+1,y))
                if i==1:
                    stack.append((x,y+1))
                if i==2:
                    stack.append((x-1,y))
                if i==3:
                    stack.append((x,y-1))

        #take the next position from the stack
        current_position= stack.pop()
    return current_position


def neighbours_to_add(current_position: Tuple[int, int], data: Any) -> bool:
    """Return the compatability of the neighbpurs to the current position (#).
          3
        4 # 2
          1
    """
    fitts=[]
    if data[current_position[0]][current_position[1]] in ["|","7","F","S"]:
        if len(data)>current_position[0]+1 and data[current_position[0]+1][current_position[1]] in ["|","L","J","S"]:
            fitts.append(True)
        else: fitts.append(False)
    else: fitts.append(False)
    if data[current_position[0]][current_position[1]] in ["-","F","L","S"]:
        if len(data[0])>current_position[1]+1 and data[current_position[0]][current_position[1]+1] in ["-","J","7","S"]:
            fitts.append(True)
        else: fitts.append(False)
    else: fitts.append(False)
    if data[current_position[0]][current_position[1]] in ["|","L","J","S"]:
        if current_position[0]>0 and data[current_position[0]-1][current_position[1]] in ["|","F","7","S"]:
            fitts.append(True)
        else: fitts.append(False)
    else: fitts.append(False)
    if data[current_position[0]][current_position[1]] in ["-","J","7","S"]:
        if current_position[1]>0 and data[current_position[0]][current_position[1]-1] in ["-","L","F","S"]:
            fitts.append(True)
        else: fitts.append(False)
    else: fitts.append(False)
    return fitts


""" def get_graph_of_pipes(pipes: Any) -> Any:
    #Return a graph of the pipes.
    graph = {}
    for pipe in pipes:
        graph[pipe] = []
        nearby= get_list_of_neighbours(pipe)
    return graph """

""" def get_list_of_neighbours(TwoDArray):
    neigh=[]
    padded=np.pad(TwoDArray,1,constant_values='.')
    for i in range(len(TwoDArray)):
        for j in range(len(TwoDArray[0])):
            area=padded[i:i+3,j:j+3]
            neigh.append(area.flatten())
    return neigh """


def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    return rek_breadth_first_search_for_pipeloop(get_start_position(data),data,[])

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""

def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input and return the solutions for part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    try:
        puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
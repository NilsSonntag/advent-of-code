from collections import deque
import pathlib
from typing import Tuple, Any, List, Dict
import numpy as np
import networkx as nx

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

def neighbors_to_add(current_position: Tuple[int, int], data: Any) -> bool:
    """Return the compatibility of the neighbors to the current position (#).
          3
        4 # 2
          1
    """
    fits=[]
    if data[current_position[0]][current_position[1]] in ["|","7","F","S"]:
        if len(data)>current_position[0]+1 and data[current_position[0]+1][current_position[1]] in ["|","L","J","S"]:
            fits.append(True)
        else: fits.append(False)
    else: fits.append(False)
    if data[current_position[0]][current_position[1]] in ["-","F","L","S"]:
        if len(data[0])>current_position[1]+1 and data[current_position[0]][current_position[1]+1] in ["-","J","7","S"]:
            fits.append(True)
        else: fits.append(False)
    else: fits.append(False)
    if data[current_position[0]][current_position[1]] in ["|","L","J","S"]:
        if current_position[0]>0 and data[current_position[0]-1][current_position[1]] in ["|","F","7","S"]:
            fits.append(True)
        else: fits.append(False)
    else: fits.append(False)
    if data[current_position[0]][current_position[1]] in ["-","J","7","S"]:
        if current_position[1]>0 and data[current_position[0]][current_position[1]-1] in ["-","L","F","S"]:
            fits.append(True)
        else: fits.append(False)
    else: fits.append(False)
    return fits

def get_graph_of_pipes(data: Any) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
    #Return a graph of the pipes.
    graph = {}
    length = len(data)
    width = len(data[0])
    for x in range(length):
        for y in range(width):
            adders = neighbors_to_add((x,y),data)
            
            if not adders[0] and not adders[1] and not adders[2] and not adders[3]:
                continue
                
            graph[(x,y)] = []
            if adders[0]:
                graph[(x,y)].append((x+1,y))
            if adders[1]:
                graph[(x,y)].append((x,y+1))
            if adders[2]:
                graph[(x,y)].append((x-1,y))
            if adders[3]:
                graph[(x,y)].append((x,y-1))
    return graph


def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    pipe_graph = get_graph_of_pipes(data)
    only_connected = pipe_graph.copy()
    for position in pipe_graph:
        if len(pipe_graph[position]) < 2:
            del only_connected[position]
    
    nx_graph = nx.Graph(only_connected)
    distance_to_start = nx.shortest_path_length(nx_graph, get_start_position(data))
    
    return max(distance_to_start.values())

def remove_not_in_cycle(pipe_graph):
    only_connected = pipe_graph.copy()
    stack = []
    
    for position in pipe_graph:
        stack.append(position)
        
        while stack:
            
            if len(pipe_graph[stack[0]]) < 2:
                stack.append(only_connected[stack[0]][0])
                del only_connected[stack[0]]
            stack.pop()
    return only_connected

def rows_to_columns(data: Any) -> Any:
    """Return the data structure with rows and columns swapped."""
    return ["".join(row) for row in zip(*data)]


def circuit_to_hashtags(data: list[str], circuit: dict[tuple[int,int],list[tuple[int,int]]]) -> list[str]:
    only_connected = remove_not_in_cycle(circuit)

    for position in only_connected:
        x,y = position
        data[x]=data[x][:y]+"#"+data[x][y+1:]
    
    return data


def shoelace(visited: list[tuple[int,int]]) -> int:
    area = sum(visited[i][0] * (visited[i - 1][1] - visited[(i + 1) % len(visited)][1]) for i in range(len(visited)))
    area = abs(area)//2
    return int(area)

def find_position_of_first_occurance(data: Any, elem: str) -> Tuple[int, int]:
    for row in data:
        if not row.find(elem)==-1:
            return (row.index(elem), data.index(row))
    return (-1, -1)

def find_path(data: Any, start_position: Tuple[int, int]) -> List[Tuple[int, int]]:
    pipe_graph = get_graph_of_pipes(data)
    only_connected = pipe_graph.copy()
    for position in pipe_graph:
        if len(pipe_graph[position]) < 2:
            del only_connected[position]
    print(only_connected)
    path = []
    #1.find a position to start from 2.from there choose one neighbor and go there 3. from there always choose the neighbor that is not the one you came from until you reach the starting position again
    #start_position = find_position_of_first_occurance(data, "S")
    path.append(start_position)
    path.append(only_connected[start_position][0])
    closed = False
    while not closed:
        current_position = path[-1]
        for x in only_connected[current_position]:
            if x != path[-2] and x != path[0]:
                path.append(x)
                break
        break
    print(path)
    return path

def find_corner_points(path : List[Tuple[int,int]]) -> List[Tuple[int, int]]:
    #remove all points where the point before and after both change the same (x or y coordinate)
    pass
        
    corner_points = []


def part2(data: Any) -> int:
    hashed = circuit_to_hashtags(data, get_graph_of_pipes(data))
    boundary_points = 0
    #!!!!!!!!calculate boundary points!!!
    interior_points = 0
    path =find_path(data, get_start_position(data))
    corners = find_corner_points(path)
    area = shoelace(path)
    interior_points = area - boundary_points//2 +1
    return interior_points



def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input and return the solutions for part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    try:
        puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
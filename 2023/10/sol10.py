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

"""
def get_graph_of_pipes(current_position: Tuple[int, int], data: Any) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
    Return the position where we first find a loop from start to start
    visited = []
    stack=[]
    graph = {}
    
    while current_position not in visited:
        graph[current_position] = []
        visited.append(current_position)
        x,y = current_position
        print(x,y)

        #find all fitting neighbors
        adders = neighbors_to_add(current_position,data)
        print(adders)

        #for all the found fitting neighbors, add them to the stack
        for i in range(0,4):
            if adders[i]:
                if i==0:
                    graph[current_position].append((x+1,y))
                    stack.append((x+1,y))
                if i==1:
                    graph[current_position].append((x,y+1))
                    stack.append((x,y+1))
                if i==2:
                    graph[current_position].append((x-1,y))
                    stack.append((x-1,y))
                if i==3:
                    graph[current_position].append((x,y-1))
                    stack.append((x,y-1))

        #take the next position from the stack
        current_position= stack.pop()
        
    print(graph)
    return graph
"""

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

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                new_path = find_shortest_path(graph, node, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest


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

""" 
def count_hashtags(data: Any) -> List[List[int]]:
    #Return the number of hashtags in the data structure
    counted = [[0 for col in range(data[0])] for row in range(data)]
    for row in data:
        for elem in row:
            if elem == "#":
                counted[data.index(row),row.index(elem):] += 1
    return counted
"""

def possible_in(data: Any) -> List[Tuple[int, int]]:
    result = []
    #counted_hashtags = count_hashtags(data)
    
    for line in data:
        parts = line.split('#')
        
        columns = []
        for i in range(len(parts)):
            current_col = sum(len(parts[j])+1 for j in range(0,i))
            if parts[i] != '':
                columns.append(current_col)
        
        parts = list(filter(lambda a: a != '', parts)) 
        
        i = 1
        while i in range(len(parts)):
            #calc current_col 
            current_col = columns[i] #TODO: check if this is correct 
            
            for a in range(len(parts[i])):
                result.append((data.index(line), current_col+a))
            
            i += 2
    
    return result

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    pipe_graph = get_graph_of_pipes(data)
    only_connected = remove_not_in_cycle(pipe_graph)

    for position in only_connected:
        x,y = position
        data[x]=data[x][:y]+"#"+data[x][y+1:]
    
    possible_in_rows = possible_in(data)
    
    cols = rows_to_columns(data)
    temp = possible_in(cols)
    possible_in_cols = [(y,x) for x,y in temp]
    
    sum_of_inner = 0
    
    for position in possible_in_rows:
            if position in possible_in_cols:
                print(position)
                sum_of_inner += 1
    
    return sum_of_inner


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
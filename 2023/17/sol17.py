import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    return puzzle_input.splitlines()


SHORTEST_PATH_FROM_START = {}

# (x,y):(len,prev_node)
D_POSSIBLE_NEXT_NODES = {}

def heat_loss_of_path(path : list) -> int:
    """Calculate the heat loss of a path."""
    return 0

def init_shortest_path_from_start(data : Any) -> None:
    """Initialize the SHORTEST_PATH_FROM_START dict containing a length and the previous position."""
    for i in range(len(data)):
        for j in range(len(data[0])):
            SHORTEST_PATH_FROM_START[(i,j)] = [int(1e9),(-1, -1)]


def get_neighbors(data,coordinate : Tuple[int,int]):
    neighbors = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 and j != 0:
                if 0 <= coordinate[0] + i < len(data) and 0 <= coordinate[1] + j < len(data[0]):  
                    neighbors.append((coordinate[0] + i, coordinate[1] + j))
    for neighbor in neighbors:
        if SHORTEST_PATH_FROM_START[neighbor][0] > SHORTEST_PATH_FROM_START[coordinate][0] + data[neighbor[0]][neighbor[1]]:
            SHORTEST_PATH_FROM_START[neighbor][0] = SHORTEST_PATH_FROM_START[coordinate][0] + data[neighbor[0]][neighbor[1]]
            SHORTEST_PATH_FROM_START[neighbor][1] = coordinate
        if neighbor not in D_POSSIBLE_NEXT_NODES and SHORTEST_PATH_FROM_START[neighbor][0] != int(1e9):
            D_POSSIBLE_NEXT_NODES[neighbor] = SHORTEST_PATH_FROM_START[coordinate][0] + data[neighbor[0]][neighbor[1]]



def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution. Basically dijkstra"""
    init_shortest_path_from_start(data)
    curr = (0,0)
    exit_found = False
    while not exit_found:
        get_neighbors(data,curr)
        # sorts the dict by size
        D_POSSIBLE_NEXT_NODES= dict(sorted(D_POSSIBLE_NEXT_NODES.items(), key=lambda item: item[1][0]))
        # get the element with the smallest distance
        next_elem = D_POSSIBLE_NEXT_NODES.popitem()
        SHORTEST_PATH_FROM_START[next_elem[0]] = next_elem[1]
        curr = next_elem[0]
        if curr = (data.length-1,data[0].length-1):
            exit_found = True
    return SHORTEST_PATH_FROM_START[curr][0]

    
        
        
        


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
        puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
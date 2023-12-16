import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    return puzzle_input.splitlines()

def get_new_position(data: Any, x:int, y:int, direction:int) -> Tuple[int, int]:
    """Get the new position and direction after following the beam."""
    if direction == 0 and y < len(data[x])-1:
        y += 1
    elif direction == 1 and x < len(data)-1:
        x += 1
    elif direction == 2 and y > 0:
        y -= 1
    elif direction == 3 and x > 0:
        x -= 1
    else:
        #found a wall
        return -1
    return x,y

def get_new_directions(data: Any, x:int, y:int, direction:int) -> int:
    """Get the new direction after following the beam.
    directions right=0, down=1, left=2, up=3"""
    if data[x][y] == '.' or (data[x][y] == '-' and direction in [0,2]) or (data[x][y] == '|' and direction in [1,3]):
        return [direction]
    if data[x][y] == '/' and direction in [1,3] or (data[x][y] == '\\' and direction in [0,2]):
        return [(direction +1) %4]
    if data[x][y] == '/' and direction in [0,2] or (data[x][y] == '\\' and direction in [1,3]):
        return [(direction - 1)%4]
    if data[x][y] == '-':
        return [0,2]
    if data[x][y] == '|':
        return [1,3]
    return -1

def follow_beam(data: Any, x:int, y:int, direction:int):
    """Follow the beam in the given direction and mark visited.
        directions right=0, down=1, left=2, up=3
    """
    direcs = get_new_directions(data,x,y,direction)
    beams = [(x,y,direc) for direc in direcs]
    while beams:
        x,y,direction = beams.pop()
        if visited[x][y][direction]:
            continue
        visited[x][y][direction] = True
        position=get_new_position(data,x,y,direction)
        if position == -1:
            continue
        x,y = position
        directions=get_new_directions(data,x,y,direction)
        for direc in directions:
            beams.append((x,y,direc))

def print_matrix(data: Any):
    """Print the matrix."""
    for row in data:
        print(row)

def get_visited_martix() -> Any:
    """Get the visited matrix."""
    visits=[]
    for x in range(len(visited)):
        visits.append([])
        for y in visited[x]:
            visits[x].append(1 if sum(y)>0 else 0)
    return visits

def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    global visited
    visits=[]
    for i in range(len(data)):
        visits.append([])
        for j in range(len(data[i])):
            visits[i].append([False for _ in range(4)])
    visited = visits
    follow_beam(data,0,0,0)
    print_matrix(get_visited_martix())
    ans=0
    for x in visited:
        for y in x:
            ans += 1 if sum(y)>0 else 0
    return ans


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
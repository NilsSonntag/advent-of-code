import pathlib
from typing import Tuple, Any
import logging

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> list[tuple[str, int, str]]:
    """Parse the puzzle input and return a data structure."""
    result = []
    lines = puzzle_input.splitlines()
    for line in lines:
        result.append(line.split(" "))
    for i in range(len(result)):
        result[i][0] = result[i][0].strip()
        result[i][1] = int(result[i][1])
        result[i][2] = result[i][2].strip().strip("(").strip(")")
        result[i] = tuple(result[i])
    return result

def log_matrix(matrix: list[str]):
    logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG, force=True, filemode='w')
    for line in matrix:
        logging.debug(line)

def dig_plan_to_coords(plan: list[tuple[str,int]]) -> list[tuple[int,int]]:
    visited = [(0,0)]
    for command in plan:
        direction, distance = command
    
        for i in range(distance):
            if direction == "R":
                visited.append((visited[-1][0]+1,visited[-1][1]))
            elif direction == "L":
                visited.append((visited[-1][0]-1,visited[-1][1]))
            elif direction == "U":
                visited.append((visited[-1][0],visited[-1][1]+1))
            elif direction == "D":
                visited.append((visited[-1][0],visited[-1][1]-1))
    
    return visited

def find_border_points(visited: list[tuple[int,int]]) -> list[int]:
    x_vals = [elem[0] for elem in visited]
    y_vals = [elem[1] for elem in visited]
    x_min = min(x_vals)
    x_max = max(x_vals)
    y_min = min(y_vals)
    y_max = max(y_vals)
    return [x_min, x_max, y_min, y_max]

def replace_at_index(string: str, index: int, replacement: str) -> str:
    return string[:index] + replacement + string[index+1:]

def coords_to_ground(coords: list[tuple[int,int]]) -> list[str]:
    ranges = find_border_points(coords)
    x_min, x_max, y_min, y_max = ranges
    ground = ["." * (x_max+1 - x_min)] * (y_max+1 - y_min)
    for coord in coords:
        x,y = coord
        ground[(y - y_min)] = replace_at_index(ground[(y - y_min)],(x - x_min),"#")
    ground.reverse()
    return ground

def print_matrix(matrix: list[str]) -> None:
    for i in range(len(matrix)):
        print(matrix[i])

def dig_out_interior(ground:list[str]) -> list[str]:
    for i in range(1,len(ground)):
        hole_count = 0
        front_up = False
        front_down = False
        for j in range(len(ground[0])):
            if ground[i][j] == ".":
                if hole_count % 2 == 1:
                    ground[i] = replace_at_index(ground[i],j,"#")
                front_down = False
                front_up = False
                continue
            
            if j+1 >= len(ground[0]):
                continue
            
            if not front_down and not front_up:
                if i-1 >= 0 and ground[i-1][j] == "#":
                    front_up = True
                if i+1 < len(ground) and ground[i+1][j] == "#":
                    front_down = True
            
            if ground[i][j+1] == "#":
                continue
            
            if i-1 >= 0 and ground[i-1][j] == "#" and front_down:
                hole_count += 1
            
            if i+1 < len(ground) and ground[i+1][j] == "#" and front_up:
                hole_count += 1

    return ground

def part1(data: list[tuple[str,int,list]]) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    visited = dig_plan_to_coords([(elem[0],elem[1]) for elem in data])
    ground = coords_to_ground(visited)
    ground = dig_out_interior(ground)
    log_matrix(ground)
    
    
    return 0

"""
..####..###.
..#..#..#.#.
###..####.#.
#.........#.
"""
"""
..####..###.
..#..#..#.#.
#########.##
#.........#.
"""

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
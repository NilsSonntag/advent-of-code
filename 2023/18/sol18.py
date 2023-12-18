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
    digged = ground.copy()
    for i in range(1,len(ground)):
        border_traversions = 0
        j=0
        while j in range(len(ground[0])):
            #cases where value at j is '.'
            if ground[i][j] == ".":
                if border_traversions % 2 == 1:
                    digged[i] = replace_at_index(digged[i],j,"#")
                j+=1
                continue
            
            #cases where value at j is '#'
            #case length of 1
            if j == len(ground[0])-1 or ground[i][j+1] == '.':
                border_traversions += 1
                j+=1
                continue

            #case length >1
            front_up = True if (i>0 and ground[i-1][j] =='#') else False
            end =False
            while j<len(ground[0])-1 and not end:
                if ground[i][j+1] == '.':
                    end =True
                else:
                    j+=1

            if ground[i-1][j] == '#':
                if not front_up:
                    border_traversions += 1
            elif front_up:
                border_traversions += 1
            
            j+=1

    return digged

def count_hole_size(hole: list[str]) -> int:
    sum=0
    for i in hole:
        sum += i.count('#')
    return sum

def part1(data: list[tuple[str,int,list]]) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    visited = dig_plan_to_coords([(elem[0],elem[1]) for elem in data])
    ground = coords_to_ground(visited)
    digged = dig_out_interior(ground)
    sum = count_hole_size(digged)
    log_matrix(digged)
    return sum


def convert_hexadezimal_to_instruction(data : str) -> tuple[str,int]:
    ans = data[1:-1]
    direction = data[-1]
    #convert ans to int
    ans = int(ans,16)
    #convert direction
    if direction == "0":
        direction = "R"
    elif direction == "1":
        direction = "D"
    elif direction == "2":
        direction = "L"
    elif direction == "3":
        direction = "U"
    return (direction,ans)

def shoelace(visited: list[tuple[int,int]]) -> int:
    area = sum(visited[i][0] * (visited[i - 1][1] - visited[(i + 1) % len(visited)][1]) for i in range(len(visited)))
    area = abs(area)//2
    return int(area)

directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    boundary_points = 0
    interior_points = 0
    visited=[(0,0)]
    for i in range(len(data)):
        direction,distance = convert_hexadezimal_to_instruction(data[i][2])
        dx, dy = directions[direction]
        boundary_points += distance
        px,py = visited[-1]
        visited.append((px+dx*distance,py+dy*distance))
    area = shoelace(visited)
    interior_points = area - boundary_points//2 +1
    return boundary_points + interior_points

    
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
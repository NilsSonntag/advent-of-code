import pathlib
from typing import Tuple, Any
import heapq as hq

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    return puzzle_input.splitlines()

# dist, x, y, px, py, moves_in_one_direction
ALREADY_SEEN = set()


def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution. Basically dijkstra"""
    ALREADY_SEEN = set()
    prioqueue = [(0, 0, 0, 0, 0, 0)]

    while prioqueue:
        dist, x, y, dx, dy, moves_in_one_direction = hq.heappop(prioqueue)
        # print(dist, x, y, dx, dy, moves_in_one_direction)
        if x == len(data) - 1 and y == len(data[0]) - 1:
            return dist
        
        if (x, y, dx, dy, moves_in_one_direction) in ALREADY_SEEN:
            continue
        
        ALREADY_SEEN.add((x, y, dx, dy, moves_in_one_direction))

        if moves_in_one_direction < 3 and (dx,dy) != (0,0) and 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]):
            hq.heappush(prioqueue, (dist + int(data[x + dx][y + dy]), x + dx, y + dy, dx, dy, moves_in_one_direction + 1))

        for (ndx, ndy) in [(-1,0),(0,-1),(1,0),(0,1)]:
            if 0 <= x + ndx < len(data) and 0 <= y + ndy < len(data[0]) and (ndx, ndy) != (dx, dy) and (-ndx, -ndy) != (dx, dy):
                hq.heappush(prioqueue, (dist + int(data[x + ndx][y + ndy]), x + ndx, y + ndy, ndx, ndy, 1))
    
    return -1


def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    """Solve part 1 of the puzzle for the given data and return the solution. Basically dijkstra"""
    ALREADY_SEEN = set()
    prioqueue = [(0, 0, 0, 0, 0, 0)]

    while prioqueue:
        dist, x, y, dx, dy, moves_in_one_direction = hq.heappop(prioqueue)
        # print(dist, x, y, dx, dy, moves_in_one_direction)
        if x == len(data) - 1 and y == len(data[0]) - 1:
            return dist
        
        if (x, y, dx, dy, moves_in_one_direction) in ALREADY_SEEN:
            continue
        
        ALREADY_SEEN.add((x, y, dx, dy, moves_in_one_direction))
        if moves_in_one_direction < 10 and (dx,dy) != (0,0) and 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]):
            hq.heappush(prioqueue, (dist + int(data[x + dx][y + dy]), x + dx, y + dy, dx, dy, moves_in_one_direction + 1))
        if 0 < moves_in_one_direction < 4:
            continue
        else:
            for (ndx, ndy) in [(-1,0),(0,-1),(1,0),(0,1)]:
                if 0 <= x + ndx < len(data) and 0 <= y + ndy < len(data[0]) and (ndx, ndy) != (dx, dy) and (-ndx, -ndy) != (dx, dy):
                    hq.heappush(prioqueue, (dist + int(data[x + ndx][y + ndy]), x + ndx, y + ndy, ndx, ndy, 1))
    
    return -1


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
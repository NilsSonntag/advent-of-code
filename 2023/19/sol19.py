import pathlib
from typing import Tuple, Any

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    puzzle_input = puzzle_input.split("\n\n")
    dict_commands = {}
    for line in puzzle_input[0].splitlines():
        line = line.split("{")
        key = line[0]
        rules = line[1].replace("}",'')
        rules = rules.split(",")
        dict_commands[key] = rules
    parts = []
    for line in puzzle_input[1].splitlines():
        for letter in ["{","}","=","x","m","a","s"]:
            line = line.replace(letter,"")
        line=line.split(",")
        line = [int(a) for a in line]
        parts.append(line)
    return (dict_commands, parts)

end_states = {"A","R"}
attributes = {"x":0,"m":1,"a":2,"s":3}

def check_if_command_applies(command : str,part) -> str:
    """Check if the command applies to the part and return the next position for that part."""
    attribute_to_check,comparison,value_to_check,successor = command[0],command[1],int(command[2]),command[-1]
    if comparison == "<":
        if part[attributes[attribute_to_check]]<value_to_check:
            return successor
    elif comparison == ">":
        if part[attributes[attribute_to_check]]>value_to_check:
            return successor
    return "not_fiting"

def reparse_command(command: Any) -> Any:
    command = command.split(":")
    check,successor = command[0],command[1]
    attribute_to_check,comparison,value_to_check = check[0],check[1],check[2:]
    return [attribute_to_check,comparison,value_to_check,successor]


def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    commands, parts = data
    ans = 0
    for part in parts:
        position = "in"
        while position not in end_states:
            for command in commands[position]:
                if command in end_states or command in commands.keys():
                    position = command
                    break
                command_list = reparse_command(command)
                result = check_if_command_applies(command_list,part)
                if result != "not_fiting":
                    position = result
                    break
        print(position)
        ans += sum(part) if position == "A" else 0
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
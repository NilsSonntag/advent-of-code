import pathlib
import pytest
import sol19 as sol
from typing import Any

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example() -> Any:
    """Read the example.txt file, parse the input, and return a data structure."""
    try:
        puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    except FileNotFoundError:
        print("The example.txt file does not exist.")
    else:
        return sol.parse(puzzle_input)

def test_parse_example(example: Any):
    """Test that input is parsed properly."""
    dict_commands = {"px":["a<2006:qkq","m>2090:A","rfg"],
                    "pv":["a>1716:R","A"],
                    "lnx":["m>1548:A","A"],
                    "rfg":["s<537:gd","x>2440:R","A"],
                    "qs":["s>3448:A","lnx"],
                    "qkq":["x<1416:A","crn"],
                    "crn":["x>2662:A","R"],
                    "in":["s<1351:px","qqz"],
                    "qqz":["s>2770:qs","m<1801:hdj","R"],
                    "gd":["a>3333:R","R"],
                    "hdj":["m>838:A","pv"]}
    parts = [[787,2655,1222,2876],
            [1679,44,2067,496],
            [2036,264,79,2244],
            [2461,1339,466,291],
            [2127,1623,2188,1013]]
    assert example == (dict_commands, parts)

def test_part1_example(example: Any):
    """Test part 1 on example input."""
    assert sol.part1(example) == 19114

@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example: Any):
    """Test part 2 on example input."""
    assert sol.part2(example) == ...
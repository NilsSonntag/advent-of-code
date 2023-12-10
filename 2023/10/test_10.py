import pathlib
import pytest
import sol10 as sol
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
    
@pytest.fixture
def example2() -> Any:
    """Read the example2.txt file, parse the input, and return a data structure."""
    try:
        puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    except FileNotFoundError:
        print("The example2.txt file does not exist.")
    else:
        return sol.parse(puzzle_input)


def test_parse_example(example: Any):
    """Test that input is parsed properly."""
    assert example  == [".....",".S-7.",".|.|.",".L-J.","....."]

def test_parse_example2(example2: Any):
    """Test that input is parsed properly."""
    assert example2  == ["..F7.",".FJ|.","SJ.L7","|F--J","LJ..."]

def test_part1_example(example: Any):
    """Test part 1 on example input."""
    assert sol.part1(example) == 4
    
def test_part1_example2(example2: Any):
    """Test part 1 on example input."""
    assert sol.part1(example2) == 8


def test_part2_example(example: Any):
    """Test part 2 on example input."""
    assert sol.part2(example) == 1
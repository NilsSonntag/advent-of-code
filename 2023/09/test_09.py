import pathlib
import pytest
import sol09 as sol
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
    assert example == [
        [0, 3, 6, 9, 12, 15], 
        [1, 3, 6, 10, 15, 21], 
        [10, 13, 16, 21, 30, 45]]

def test_part1_example(example: Any):
    """Test part 1 on example input."""
    assert sol.part1(example) == 114

@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example: Any):
    """Test part 2 on example input."""
    assert sol.part2(example) == ...
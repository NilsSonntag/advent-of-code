import pathlib
import pytest
import sol11 as sol
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
    assert example == ["...#......", ".......#..", "#.........", "..........", "......#...", ".#........", ".........#", "..........", ".......#..", "#...#....."]

def test_part1_example(example: Any):
    """Test part 1 on example input."""
    assert sol.part1(example) == 374

def test_part2_example(example: Any):
    """Test part 2 on example input."""
    assert sol.part2(example, 100) == 8410
import pathlib
import pytest
import template as sol
from typing import Any

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example(number: int) -> Any:
    """Read the example{number}.txt file, parse the input, and return a data structure."""
    try:
        puzzle_input = (PUZZLE_DIR / f"example{number}.txt").read_text().strip()
    except FileNotFoundError:
        print(f"The example{number}.txt file does not exist.")
    else:
        return sol.parse(puzzle_input)

@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example: Any):
    """Test that input is parsed properly."""
    assert example(1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example: Any):
    """Test part 1 on example1 input."""
    assert sol.part1(example(1)) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example: Any):
    """Test part 2 on example1 input."""
    assert sol.part2(example(1)) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example: Any):
    """Test part 2 on example2 input."""
    assert sol.part2(example(2)) == ...
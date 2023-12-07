import pathlib
import pytest
import sol07 as sol
from typing import Any

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return sol.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return sol.parse(puzzle_input)

def test_parse_example1(example1: Any):
    """Test that input is parsed properly."""
    assert example1 == [(['3','2','T','3','K'], 765), (['T','5','5','J','5'], 684), (['K','K','6','7','7'], 28), (['K','T','J','J','T'], 220), (['Q','Q','Q','J','A'], 483)]

def test_part1_example1(example1: Any):
    """Test part 1 on example1 input."""
    assert sol.part1(example1) == 6440

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example: Any):
    """Test part 2 on example1 input."""
    assert sol.part2(example(1)) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example: Any):
    """Test part 2 on example2 input."""
    assert sol.part2(example(2)) == ...
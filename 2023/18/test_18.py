import pathlib
import pytest
import sol18 as sol
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
    assert example == [['R',6,"#70c710"],["D",5,"#0dc571"],["L",2,"#5713f0"],["D",2,"#d2c081"],["R",2,"#59c680"],["D",2,"#411b91"],["L",5,"#8ceee2"],["U",2,"#caa173"],["L",1,"#1b58a2"],["U",2,"#caa171"],["R",2,"#7807d2"],["U",3,"#a77fa3"],["L",2,"#015232"],["U",2,"#7a21e3"]]


def test_part1_example(example: Any):
    """Test part 1 on example input."""
    assert sol.part1(example) == 62

@pytest.mark.skip(reason="Not implemented")
def test_part2_example(example: Any):
    """Test part 2 on example input."""
    assert sol.part2(example) == ...
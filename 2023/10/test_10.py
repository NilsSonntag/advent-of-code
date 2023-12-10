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
@pytest.fixture
def example3() -> Any:
    """Read the example3.txt file, parse the input, and return a data structure."""
    try:
        puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    except FileNotFoundError:
        print("The example.txt file does not exist.")
    else:
        return sol.parse(puzzle_input)
    
@pytest.fixture
def example4() -> Any:
    """Read the example4.txt file, parse the input, and return a data structure."""
    try:
        puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    except FileNotFoundError:
        print("The example2.txt file does not exist.")
    else:
        return sol.parse(puzzle_input)


def test_parse_example(example: Any):
    """Test that input is parsed properly."""
    assert example  == [".....",".S-7.",".|.|.",".L-J.","....."]

def test_part1_example(example: Any):
    """Test part 1 on example input."""
    assert sol.part1(example) == 4


def test_part1_example2(example2: Any):
    """Test part 1 on example input."""
    assert sol.part1(example2) == 8

def test_part2_example3(example3: Any):
    """Test part 2 on example input."""
    assert sol.part2(example3) == 4
    
@pytest.mark.skip("Not implemented yet.")  
def test_part2_example4(example4: Any):
    """Test part 2 on example input."""
    assert sol.part2(example4) == 8
    
@pytest.mark.skip("Not implemented yet.")
def test_part2_example5(example5: Any):
    """Test part 2 on example input."""
    assert sol.part2(example) == ...
import pathlib
import pytest
import sol02 as sol

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return sol.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return sol.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {1: "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 2: "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 3: "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 4: "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 5: "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"}

def test_part1_example1(example1):
    """Test part 1 on example1 input."""
    assert sol.part1(example1) == 8

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example1 input."""
    assert sol.part2(example1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example2 input."""
    assert sol.part2(example2) == ...
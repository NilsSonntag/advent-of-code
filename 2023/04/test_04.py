import pathlib
import pytest
import sol04 as sol

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
    ls1 = [[41,48,83,86,17], [13, 32, 20, 16, 61], [1, 21, 53, 59, 44], [41, 92, 73, 84, 69], [87, 83, 26, 28, 32],[31, 18, 13, 56, 72]]
    ls2 =  [[83, 86, 6, 31, 17, 9, 48, 53], [61, 30, 68, 82, 17, 32, 24, 19], [69, 82, 63, 72, 16, 21, 14, 1], [59, 84, 76, 51, 58, 5, 54, 83], [88, 30, 70, 12, 93, 22, 82, 36], [74, 77, 10, 23, 35, 67, 36, 11]]
    assert example1 == (ls1, ls2)

def test_part1_example1(example1):
    """Test part 1 on example1 input."""
    assert sol.part1(example1) == 13

def test_part2_example1(example1):
    """Test part 2 on example1 input."""
    assert sol.part2(example1) == 30

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example2 input."""
    assert sol.part2(example2) == ...
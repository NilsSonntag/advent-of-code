import pathlib
import pytest
import sol03 as sol
import numpy as np

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
    sollte_so_aussehen =np.array([['4','6','7','.','.','1','1','4','.','.'], ['.','.','.','*','.','.','.','.','.','.'], ['.', '.', '3', '5','.','.','6','3','3','.'], ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'], ['6','1','7','*','.','.','.','.','.','.'], ['.','.', '.', '.', '.', '#', '.', '5', '8', '.'], ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'], ['.', '.', '.', '#', '.', '*', '.', '.', '.', '.'], ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']])
    assert (example1 == sollte_so_aussehen).all()

def test_part1_example1(example1):
    """Test part 1 on example1 input."""
    assert sol.part1(example1) == 4361

def test_part2_example1(example1):
    """Test part 2 on example1 input."""
    assert sol.part2(example1) == 467835

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example2 input."""
    assert sol.part2(example2) == ...
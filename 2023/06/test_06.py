import pathlib
import pytest
import sol06 as sol

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
    inputs = [(7,9),(15,40),(30,200)]
    assert example1 == inputs


def test_part1_example1(example1):
    """Test part 1 on example1 input."""
    assert sol.part1(example1) == 288

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example1 input."""
    assert sol.part2(example1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example2 input."""
    assert sol.part2(example2) == ...
import pathlib
import pytest
import sol12 as sol
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
    assert example == (["???.###",".??..??...?##.","?#?#?#?#?#?#?#?","????.#...#...","????.######..#####.","?###????????"],[[1,1,3],[1,1,3],[1,3,1,6],[4,1,1],[1,6,5],[3,2,1]])

def test_get_error_struct(example: Any):
    """Test get_error_struct on example input."""
    error_struct = [[3],[2],[1,1,1,1,1,1,1],[1,1],[6,5],[3]]
    for i in range(len(example[0])):
        springs = example[0][i]
        assert sol.get_error_struct(springs) == error_struct[i]

def test_unfold(example: Any):
    """Test unfold on example input."""
    springs, error_struct = sol.unfold(example)
    assert springs == ["???.###????.###????.###????.###????.###",
                       ".??..??...?##.?.??..??...?##.?.??..??...?##.?.??..??...?##.?.??..??...?##.",
                       "?#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#???#?#?#?#?#?#?#?",
                       "????.#...#...?????.#...#...?????.#...#...?????.#...#...?????.#...#...",
                       "????.######..#####.?????.######..#####.?????.######..#####.?????.######..#####.?????.######..#####.",
                       "?###??????????###??????????###??????????###??????????###????????"]
    assert error_struct == [[1,1,3,1,1,3,1,1,3,1,1,3,1,1,3],[1,1,3,1,1,3,1,1,3,1,1,3,1,1,3],
                            [1,3,1,6,1,3,1,6,1,3,1,6,1,3,1,6,1,3,1,6],[4,1,1,4,1,1,4,1,1,4,1,1,4,1,1],
                            [1,6,5,1,6,5,1,6,5,1,6,5,1,6,5],[3,2,1,3,2,1,3,2,1,3,2,1,3,2,1]]

def test_part1_example(example: Any):
    """Test part 1 on example input."""
    assert sol.part1(example) == 21

def test_part2_example(example: Any):
    """Test part 2 on example input."""
    assert sol.part2(example) == 525152
import pathlib
import pytest
import sol05 as sol

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
    seeds = [79, 14, 55, 13]

    seedSoil =[[50, 98, 2], [52, 50, 48]]

    soilFertilizer = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]

    fertilizerWater = [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]]
    waterLight = [[88, 18, 7], [18, 25, 70]]

    lightTemperature = [[45, 77, 23],[81, 45, 19],[68, 64, 13]]

    temperatureHumidity = [[0, 69, 1], [1, 0, 69]]

    humidityLocation = [[60, 56, 37],[56, 93, 4]]
    assert example1 == [seeds, seedSoil, soilFertilizer, fertilizerWater, waterLight, lightTemperature, temperatureHumidity, humidityLocation]


def test_part1_example1(example1):
    """Test part 1 on example1 input."""
    assert sol.part1(example1) == 35

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example1 input."""
    assert sol.part2(example1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example2 input."""
    assert sol.part2(example2) == ...
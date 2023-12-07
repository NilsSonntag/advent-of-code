import pathlib
from typing import List, Tuple, Any
from collections import Counter

PUZZLE_DIR = pathlib.Path(__file__).parent

def parse(puzzle_input: str) -> Any:
    """Parse the puzzle input and return a data structure."""
    lines = puzzle_input.splitlines()
    result = [(line.split(" ")[0], line.split(" ")[1]) for line in lines]
    result = [(hand, int(score)) for hand, score in result]
    for i in range(len(result)):
        result[i] = (list(result[i][0]), result[i][1])
    return result

def find_type(hand) -> int:
    """Find the type of the puzzle input and return it as an integer."""
    order=Counter(hand).keys()
    frequency=list(Counter(hand).values())
    if len(order)==1: return 6
    elif len(order)==2: 
        if 4 in frequency: 
            return 5
        else:
            return 4
    elif len(order)==3:
        if 3 in frequency:
            return 3
        else:
            return 2
    elif 2 in frequency:
        return 1
    else: return 0

def hand_value(pair: List[str]) -> int:
    """Calculate the value of the given hand and return it as an integer."""
    hand = pair[0]
    digits = [0,0,0,0,0]
    for i in range(5):
        if hand[i].isdigit():
            digits[i] = ('0' + hand[i])
            continue
        if hand[i] == "A":
            digits[i] = '14'
        elif hand[i] == "K":
            digits[i] = '13'
        elif hand[i] == "Q":
            digits[i] = '12'
        elif hand[i] == "J":
            digits[i] = '11'
        elif hand[i] == "T":
            digits[i] = '10'
    result = "".join(digits)
    return int(result)

def calculate_score_from_level(hand_level_sorted,rank_of_first) -> int:
    """Calculate the score of the given hand level and return it."""
    score = 0
    for i in range(len(hand_level_sorted)):
        score += (i+rank_of_first)*hand_level_sorted[i][1]
    return score

def part1(data: Any) -> int:
    """Solve part 1 of the puzzle for the given data and return the solution."""
    score = 0
    hand_of_index_level = [[],[],[],[],[],[],[]]
    rank_of_index_level = 1
    for entry in data:
        hand_of_index_level[find_type(entry[0])].append(entry)
    #sort all the levels by value of the hand
    for index_level in hand_of_index_level:
        index_level.sort(key = hand_value)
        score += calculate_score_from_level(index_level, rank_of_index_level)
        rank_of_index_level += len(index_level)
    return score

def find_type_with_joker(hand) -> int:
    """Find the type of the puzzle input and return it as an integer."""
    amount_of_jokers = hand.count("J")
    there_is_a_joker = amount_of_jokers > 0
    order=Counter(hand).keys()
    frequency=list(Counter(hand).values())
    different_cards = len(order) - there_is_a_joker
    if different_cards<=1: return 6
    elif different_cards==2: 
        if (4-amount_of_jokers) in frequency: 
            return 5
        else:
            return 4
    elif different_cards==3:
        if (3-amount_of_jokers) in frequency:
            return 3
        else:
            return 2
    elif (2-amount_of_jokers) in frequency:
        return 1
    else: return 0
    
def hand_value_with_joker(pair: List[str]) -> int:
    """Calculate the value of the given hand and return it as an integer."""
    hand = pair[0]
    digits = [0,0,0,0,0]
    for i in range(5):
        if hand[i].isdigit():
            digits[i] = ('0' + hand[i])
            continue
        if hand[i] == "A":
            digits[i] = '14'
        elif hand[i] == "K":
            digits[i] = '13'
        elif hand[i] == "Q":
            digits[i] = '12'
        elif hand[i] == "T":
            digits[i] = '10'
        elif hand[i] == "J":
            digits[i] = '01'
    result = "".join(digits)
    return int(result)

def part2(data: Any) -> int:
    """Solve part 2 of the puzzle for the given data and return the solution."""
    score = 0
    hand_of_index_level = [[],[],[],[],[],[],[]]
    rank_of_index_level = 1
    for entry in data:
        hand_of_index_level[find_type_with_joker(entry[0])].append(entry)
    #sort all the levels by value of the hand
    for index_level in hand_of_index_level:
        index_level.sort(key = hand_value_with_joker)
        score += calculate_score_from_level(index_level, rank_of_index_level)
        rank_of_index_level += len(index_level)
    return score

def solve(puzzle_input: str) -> Tuple[int, int]:
    """Solve the puzzle for the given input and return the solutions for part 1 and part 2."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    try:
        puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    except FileNotFoundError:
        print("The input file does not exist.")
    else:
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
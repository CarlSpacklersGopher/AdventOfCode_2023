import re

def process_input(path: str) -> list:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        return f.readlines()

def part_1(puzzle_input: list) -> int:
    ''' Solves for part 1. '''
    calibrations = []
    for calibration_value in puzzle_input:
        numbers = re.findall(r'\d', calibration_value)
        calibrations.append(int(numbers[0] + numbers[-1]))
    return sum(calibrations)

def part_2(puzzle_input: list) -> int:
    ''' Solves for part 2.  '''
    pass

if __name__ == "__main__":
    # puzzle_input = process_input('01/test_input1.txt')
    puzzle_input = process_input('01/test_input2.txt')
    # puzzle_input = process_input('01/input.txt')
    pt1 = part_1(puzzle_input)
    print("Part 1: " + str(pt1))


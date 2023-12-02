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
    calibrations = []
    for calibration_line in puzzle_input:
        numbers = extract_numbers(calibration_line)
        calibrations.append(int(numbers[0] + numbers[-1]))
    return sum(calibrations)

def extract_numbers(calibration_line:str) -> str:
    ''' Extracts all digits and spelled out numbers from the string.  Returns a list with
    the last digit of each detected number. '''
    spellings_dict = {'zero'    :'0',
                      'one'     :'1',
                      'two'     :'2',
                      'three'   :'3',
                      'four'    :'4',
                      'five'    :'5',
                      'six'     :'6',
                      'seven'   :'7',
                      'eight'   :'8',
                      'nine'    :'9',
                      'ten'     :'0',
                      'eleven'  :'1',
                      'twelve'  :'2',
                      'thirteen':'3'
                     }
    pattern = r'(\d|' + '|'.join(spellings_dict.keys()) + ')' # match any digit or number text
    pattern = r'(?=' + pattern + ')' # match overlapping strings - ex "zerone" matches "zero" and "one"
    digits_and_spellings = re.findall(pattern, calibration_line)
    only_digits = [x if x.isdigit() else spellings_dict[x] for x in digits_and_spellings]
    return only_digits



if __name__ == "__main__":
    # puzzle_input = process_input('01/test_input1.txt')
    puzzle_input = process_input('01/input.txt')
    pt1 = part_1(puzzle_input)
    print("Part 1: " + str(pt1))

    # puzzle_input = process_input('01/test_input2.txt')
    pt2 = part_2(puzzle_input)
    print("Part 2: " + str(pt2))


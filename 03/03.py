import re

def process_input(path: str) -> list:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        return f.readlines()

def look_around(match: re.Match, match_line: int, search_field: list[str], pattern:str) -> list[re.Match]:
    '''
    Searches the locations surrounding the match (up, down, immediate left, immediate right,
    diagonals) for anything matching the pattern.  Search does not wrap around.
    Returns list of the matches.
    '''
    left_pos = max(0, match.start() - 1)
    right_pos = min(len(search_field[match_line]) - 1, match.end() + 1)
    top_pos = max(0, match_line - 1)
    bottom_pos = min(len(search_field) - 1, match_line + 1)

    lines = [search_field[top_pos][left_pos:right_pos],
             search_field[match_line][left_pos],
             search_field[match_line][right_pos - 1],
             search_field[bottom_pos][left_pos:right_pos]
             ]

    matches = []
    for line in lines:
        line_matches = re.findall(pattern, line)
        matches.append([match for match in line_matches])
    no_matches = [[], [], [], []]
    return matches if matches != no_matches else [] # allow caller to check "if matches:"



def part_1(lines: list[str]) -> int:
    ''' Solves for part 1. '''
    part_numbers = []
    for line_num, line in enumerate(lines):
        digit_pattern = r'\d+'
        symbol_pattern = r'[^.\d\n]' # non-period, non-digit, non-newline characters
        match_iter = re.finditer(digit_pattern, line)
        for match in match_iter:
            matches = look_around(match, line_num, lines, symbol_pattern)
            if matches:
                part_numbers.append(int(match[0]))
    return sum(part_numbers)


def part_2(lines: list[str]) -> int:
    ''' Solves for part 2.  '''
    return 0

if __name__ == "__main__":
    # puzzle_input = process_input('03/test_input.txt')
    puzzle_input = process_input('03/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))


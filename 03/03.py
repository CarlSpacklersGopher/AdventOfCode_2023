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
    right_pos = min(len(search_field[match_line]) - 1, match.end())
    top_pos = max(0, match_line - 1)
    bottom_pos = min(len(search_field) - 1, match_line + 1)

    window_matches = [expand_search(search_field[top_pos], left_pos, right_pos, pattern),
                      expand_search(search_field[match_line], left_pos, left_pos, pattern), # look left
                      expand_search(search_field[match_line], right_pos, right_pos, pattern), # look right
                      expand_search(search_field[bottom_pos], left_pos, right_pos, pattern),
                      ]

    matches = []
    no_matches = ['', '', '', '']
    if window_matches == no_matches:
        return matches
    for match_str in window_matches:
        if match_str:
            line_matches = re.findall(pattern, match_str)
            matches.append(list(line_matches))
    return matches


def expand_search(search_field:str, window_start:int, window_end:int, pattern:str) -> str:
    ''' Gets an expanded search area so matches that start before / end after the match's adjacent
    positions aren't cut off.

    I don't really care for this implementation - you end up looping through the whole line multiple
    times, but couldn't think of a way to look back/forward a single character at a time that
    respects an arbitrary regex.  Can't look backwards - aren't sure if the regex has + or not.
    '''
    matches_in_window = []
    entered_window = False
    exited_window = False
    for m in re.finditer(pattern, search_field):
        entered_window = m.end() - 1 >= window_start
        exited_window = m.start() > window_end
        if exited_window: break
        if entered_window:
            matches_in_window.append(m)
    if matches_in_window:
        return search_field[matches_in_window[0].start() : matches_in_window[-1].end()]
    else:
        return ''


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

def flatten(l: list[list]) -> list:
    ''' Flattens a simple 2D list into a single list.'''
    return [item for sublist in l for item in sublist]

def part_2(lines: list[str]) -> int:
    ''' Solves for part 2.  '''
    gear_ratios = []
    for line_num, line in enumerate(lines):
        digit_pattern = r'\d+'
        gear_pattern = r'\*'
        match_iter = re.finditer(gear_pattern, line)
        for match in match_iter:
            matches = look_around(match, line_num, lines, digit_pattern)
            flat_list = flatten(matches)
            if len(flat_list) == 2:
                gear_ratios.append(int(flat_list[0]) * int(flat_list[1]))
    return sum(gear_ratios)

if __name__ == "__main__":

    # puzzle_input = process_input('03/test_input.txt')
    puzzle_input = process_input('03/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))
    '''
    testinput=[
                '.!..12345.',
                '.#.67*89..',
                '.%.0...1..',
               ]
    line=1
    numbers = re.finditer(r'[^.\d\n]', testinput[line])
    for m in numbers:
        surrounding_matches = look_around(m, line, testinput, r'\d+')
    print(surrounding_matches)
    '''



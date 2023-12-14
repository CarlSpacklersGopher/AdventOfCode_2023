

def process_input(path: str) -> list[str]:
    ''' Reads the puzzle input. '''
    with open(path) as f:
        data = f.read()
        patterns = data.split('\n\n')

        pattern_list = []
        for pattern in patterns:
            pattern_list.append(pattern.split('\n'))
        return pattern_list

def get_mirror_line(lines: list[str]) -> int:
    for line_num, line in enumerate(lines):
        if line_num == 0:
            continue
        if line == lines[line_num - 1]:
            left_part = lines[:line_num]
            right_part = lines[line_num:]

            search_width = min(len(left_part), len(right_part))

            left_part = left_part[-1 * search_width :]
            right_part = right_part[:search_width]

            left_part.reverse()
            if left_part == right_part:
                return line_num
    return 0



def part_1(puzzle_input:list[tuple]) -> int:
    ''' Solves for Part 1. '''
    mirror_scores = []
    for idx, pattern in enumerate(puzzle_input):
        horiz_mirror_line = get_mirror_line(pattern)
        transposed_pattern = [''.join(i) for i in zip(*pattern)]
        vert_mirror_line = get_mirror_line(transposed_pattern)

        print(f'Grid {idx+1}, Matching Row: {horiz_mirror_line}, Matching Column: {vert_mirror_line}')

        mirror_scores.append(vert_mirror_line + (100 * horiz_mirror_line))
    return sum(mirror_scores)

def part_2(puzzle_input:list[str]) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    # puzzle_input = process_input('13/test_input.txt')
    puzzle_input = process_input('13/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))

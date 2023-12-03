

def process_input(path: str) -> list:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        return f.readlines()


def part_1(lines: list[str]) -> int:
    ''' Solves for part 1. '''
    return 0



def part_2(lines: list[str]) -> int:
    ''' Solves for part 2.  '''
    return 0

if __name__ == "__main__":
    # puzzle_input = process_input('02/test_input.txt')
    puzzle_input = process_input('02/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))



def process_input(path: str) -> list[list]:
    ''' Reads the puzzle input. '''
    galaxies = []
    with open(path) as f:
        for line_num, line in enumerate(f):
            for char_num, char in enumerate(line):
                if char == '#': # Galaxy found
                    galaxies.append([line_num, char_num])
    return galaxies

def cosmic_expansion_onedir(galaxies:list[list], NS_EW:str, expansion:int) -> None:
    ''' Gets new locations of each galaxy after expansion. Directly modifies galaxies input'''
    lookup = 0 if NS_EW == 'NS' else 1

    galaxies.sort(key=lambda galaxy: galaxy[lookup]) # Sort on rows/cols for empty detection
    last_occupied = 0
    cosmic_expansion = 0
    for galaxy in galaxies:
        current = galaxy[lookup]
        if current - last_occupied > 1:
            cosmic_expansion += expansion * (current - last_occupied - 1)
        galaxy[lookup] += cosmic_expansion
        last_occupied = current
    return galaxies

def get_total_distance(galaxies: list[list]) -> int:
    ''' Calculates total distance between all pairs of galaxies, assuming one step up, down, left,
    or right at a time.  '''
    total_distance = 0
    for idx, start_galaxy in enumerate(galaxies):
        for target_galaxy in galaxies[idx:]:
            total_distance += abs(start_galaxy[0] - target_galaxy[0])
            total_distance += abs(start_galaxy[1] - target_galaxy[1])
    return total_distance

def part_1(galaxies:list[list]) -> int:
    ''' Solves for Part 1. '''
    # Expand the universe
    cosmic_expansion_onedir(galaxies, 'NS', 1)
    cosmic_expansion_onedir(galaxies, 'EW', 1)

    return get_total_distance(galaxies)

def part_2(galaxies:list[list], expansion:int) -> int:
    ''' Solves for Part 2. '''
    # Expand the universe
    cosmic_expansion_onedir(galaxies, 'NS', expansion)
    cosmic_expansion_onedir(galaxies, 'EW', expansion)

    return get_total_distance(galaxies)

if __name__ == '__main__':
    # puzzle_input = process_input('11/test_input.txt')
    puzzle_input = process_input('11/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    # puzzle_input = process_input('11/test_input.txt')
    puzzle_input = process_input('11/input.txt')
    print("Part 2: " + str(part_2(puzzle_input, 1000000-1)))

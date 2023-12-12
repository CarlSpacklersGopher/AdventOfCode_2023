

def process_input(path: str) -> list[list]:
    ''' Reads the puzzle input. '''
    galaxies = []
    with open(path) as f:
        for line_num, line in enumerate(f):
            for char_num, char in enumerate(line):
                if char == '#': # Galaxy found
                    galaxies.append([line_num, char_num])
    return galaxies

def part_1(galaxies:list[list]) -> int:
    ''' Solves for Part 1. '''
    # Expand Universe North-South
    galaxies.sort(key=lambda galaxy: galaxy[0]) # Sort on rows
    last_occupied_row = 0
    cosmic_expansion = 0
    for galaxy in galaxies:
        current_row = galaxy[0]
        if current_row - last_occupied_row > 1:
            cosmic_expansion += current_row - last_occupied_row - 1
        galaxy[0] += cosmic_expansion
        last_occupied_row = current_row

    # Expand Universe East-West
    galaxies.sort(key=lambda galaxy: galaxy[1]) # Sort on cols
    last_occupied_col = 0
    cosmic_expansion = 0
    for galaxy in galaxies:
        current_col = galaxy[1]
        if current_col - last_occupied_col > 1:
            cosmic_expansion += current_col - last_occupied_col - 1
        galaxy[1] += cosmic_expansion
        last_occupied_col = current_col

    # Calculate Distances
    total_distance = 0
    for idx, start_galaxy in enumerate(galaxies):
        for target_galaxy in galaxies[idx:]:
            total_distance += abs(start_galaxy[0] - target_galaxy[0])
            total_distance += abs(start_galaxy[1] - target_galaxy[1])
    return total_distance

def part_2(puzzle_input:list[str]) -> int:
    ''' Solves for Part 2. '''
    return 0

if __name__ == '__main__':
    # puzzle_input = process_input('11/test_input.txt')
    puzzle_input = process_input('11/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))

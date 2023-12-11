import math

def process_input(path: str) -> list[str]:
    ''' Reads the puzzle input. '''
    with open(path) as f:
        return f.readlines()

def get_locations(locations:list[str]) -> dict:
    ''' Returns a dictionary with keys=locations and values = tuple. '''
    location_dict = {}
    for location_str in locations:
        location, loc_tuple = location_str.strip().split(' = ')
        loc1, loc2 = loc_tuple[1:-1].split(', ')
        location_dict[location] = (loc1, loc2)

    return location_dict


def part_1(puzzle_input:list[str]) -> int:
    ''' Solves for Part 1. '''
    directions = [direction for direction in puzzle_input[0].strip()]
    location_dict = get_locations(puzzle_input[2:])

    current_location = 'AAA'
    end_location = 'ZZZ'
    visited = []

    while True:
        for direction in directions:
            if current_location == end_location:
                return len(visited)
            current_location = get_next_location(direction, location_dict, current_location)
            visited.append(current_location)

def get_next_location(direction:str, location_map:dict, current_location:str) -> str:
    lookup = 0 if direction == 'L' else 1
    next_location = location_map[current_location][lookup]
    return next_location

def part_2(puzzle_input:list[str]) -> int:
    ''' Solves for Part 2. '''
    directions = [direction for direction in puzzle_input[0].strip()]
    location_dict = get_locations(puzzle_input[2:])

    current_locations = []
    for key in location_dict:
        if key.endswith('A'):
            current_locations.append(key)

    visit_counts = []
    for location in current_locations:
        visited = []
        break_out = False
        while not break_out:
            for direction in directions:
                if location.endswith('Z'):
                    visit_counts.append(len(visited))
                    break_out = True
                    break
                location = get_next_location(direction, location_dict, location)
                visited.append(location)

    return math.lcm(*visit_counts)


if __name__ == '__main__':
    # puzzle_input = process_input('08/test_input.txt')
    puzzle_input = process_input('08/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    # puzzle_input = process_input('08/test_input3.txt')
    print("Part 2: " + str(part_2(puzzle_input)))

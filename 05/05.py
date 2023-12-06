import time

def process_input(path: str) -> dict:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        contents = f.read()
        map_chunks = contents.split('\n\n') # blank line divider between map chunks
        map_dict = {}

        seed_str = map_chunks[0].split()[1:] # ignore "seed: "
        map_dict['seed'] = [int(seed) for seed in seed_str]

        for map_chunk in map_chunks[1:]: # Skip seed
            lines = map_chunk.split('\n')
            label = lines[0].split('-')[-1][:-5] # get destination, strip " map:"
            dest_src_range = []
            for line in lines[1:]: # First line is label
                dest_src_range.append([int(x) for x in line.split()])
            map_dict[label] = dest_src_range
        return map_dict

def find_destination(src_in: int, almanac_map: list[list[int]]) -> int:
    for almanac_line in almanac_map:
        dest_min, src_min, rng = almanac_line
        src_max = src_min + rng - 1
        # Take seed.  Determine which source range it's in
        if src_min <= src_in <= src_max:
            offset = src_in - src_min # Determine offset from bottom of range.
            return dest_min + offset  # Lookup new destination - offset from dest range min
    return src_in # no mapping applied


def part_1(map_dict: dict) -> int:
    ''' Solves for part 1. '''
    locations = []
    for seed in map_dict['seed']:
        soil = find_destination(seed, map_dict['soil'])
        fertilizer = find_destination(soil, map_dict['fertilizer'])
        water = find_destination(fertilizer, map_dict['water'])
        light = find_destination(water, map_dict['light'])
        temperature = find_destination(light, map_dict['temperature'])
        humidity = find_destination(temperature, map_dict['humidity'])
        location = find_destination(humidity, map_dict['location'])

        locations.append(location)

        '''
        # Print for debug purposes
        s =  'Seed {}, '.format(seed)
        s += 'soil {}, '.format(soil)
        s += 'fertilizer {}, '.format(fertilizer)
        s += 'water {}, '.format(water)
        s += 'light {}, '.format(light)
        s += 'temperature {}, '.format(temperature)
        s += 'humidity {}, '.format(humidity)
        s += 'location {}.'.format(location)

        print(s)
        '''


    return min(locations)

def part_2(puzzle_input: list[str]) -> int:
    ''' Solves for part 2.  '''
    return 0


if __name__ == "__main__":
    start = time.time()
    # puzzle_input = process_input('05/test_input.txt')
    puzzle_input = process_input('05/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))
    end = time.time()
    print("Part 1 time: " + str(end - start)) # 0.001

    print("Part 2: " + str(part_2(puzzle_input)))



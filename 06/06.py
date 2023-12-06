from math import prod

def process_input(path: str) -> zip:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        lines = f.readlines()
        times = [int(x) for x in lines[0].split()[1:]]
        distances = [int(x) for x in lines[1].split()[1:]]
        return zip(times, distances)

def part_1(race_records: zip) -> int:
    ''' Solves for part 1. '''
    winning_combinations = []
    for time, record_distance in race_records:
        # dist = charge_time * (time - charge_time)
        # just gonna brute force this one
        win_count = 0
        for charge_time in range(time):
            my_distance = charge_time * (time - charge_time)
            if my_distance > record_distance:
                win_count += 1
        winning_combinations.append(win_count)
    print(winning_combinations)
    return prod(winning_combinations)

def part_2(puzzle_input: list[str]) -> int:
    ''' Solves for part 2.  '''
    return 0


if __name__ == "__main__":
    # puzzle_input = process_input('06/test_input.txt')
    puzzle_input = process_input('06/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))



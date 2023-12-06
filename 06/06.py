import math

def process_split_input(path: str) -> zip:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        lines = f.readlines()
        times = [int(x) for x in lines[0].split()[1:]]
        distances = [int(x) for x in lines[1].split()[1:]]
        return zip(times, distances)

def process_combined_input(path: str) -> tuple[int]:
    ''' Reads the puzzle input. '''
    with open(path, 'r') as f:
        lines = f.readlines()
        time = int(''.join(lines[0].split()[1:]))
        distance = int(''.join(lines[1].split()[1:]))
        return (time, distance)

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
    return math.prod(winning_combinations)

def part_2(race_record: tuple[int]) -> int:
    ''' Solves for part 2.  '''
    # dist = charge_time * (time - charge_time)
    #   0  = -charge_time**2 + time*charge_time - dist
    #   0  = charge_time**2 - time*charge_time + dist
    # find max dist by taking derivative wrt charge_time
    # dist' = 2*charge_time - time
    # charge_time = time/2 to yield max distance
    time, distance = race_record
    optimal_charge_time = time / 2
    # charge_time to get current record - solve with quadratic formula
    record_charge_time = (time + math.sqrt((-1*time)**2 - 4 * (1) * distance)) / (2 * 1)

    # symmetrical on both sides
    winning_time_count = round(2 * abs(record_charge_time - optimal_charge_time))
    return winning_time_count


if __name__ == "__main__":
    # puzzle_input = process_split_input('06/test_input.txt')
    puzzle_input = process_split_input('06/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    # puzzle_input = process_combined_input('06/test_input.txt')
    puzzle_input = process_combined_input('06/input.txt')
    print("Part 2: " + str(part_2(puzzle_input)))



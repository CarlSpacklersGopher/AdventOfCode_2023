import pprint

def process_input(path: str) -> zip:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        winners = []
        card_numbers = []
        for line in f:
            winner_chunk, my_chunk = line.split('|')
            winners.append(winner_chunk.split()[2:]) # Split off "Card x:"
            card_numbers.append(my_chunk.split())
    return zip(winners, card_numbers)

def part_1(cards: zip) -> int:
    ''' Solves for part 1. '''
    card_points = []
    for winners, card_numbers in cards:
        win_count = 0
        for winning_number in winners:
            for my_number in card_numbers:
                if int(winning_number) == int(my_number):
                    win_count += 1
        card_points.append(0 if win_count == 0 else 2 ** (win_count - 1))

    return sum(card_points)

def part_2(lines: list[str]) -> int:
    ''' Solves for part 2.  '''
    return 0

if __name__ == "__main__":

    # puzzle_input = process_input('04/test_input.txt')
    puzzle_input = process_input('04/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))



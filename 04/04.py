
def process_input(path: str) -> dict:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        COPIES = 1
        card_dict = {}
        for idx, line in enumerate(f):
            winner_chunk, my_chunk = line.split('|')
            winners = winner_chunk.split()[2:]
            card_numbers = my_chunk.split()
            card_dict[idx + 1] = [COPIES, winners, card_numbers]
    return card_dict

def part_1(cards: dict) -> int:
    ''' Solves for part 1. '''
    # Using sets is fast, but might get weird if we have duplicates in the card's numbers that win
    card_points = []
    for _, winners, card_numbers in cards.values():
        wins = count_wins(winners, card_numbers)
        card_points.append(0 if wins == 0 else 2 ** (wins - 1))

    return sum(card_points)

def count_wins(winning_numbers: list[int], my_numbers: list[int]) -> int:
        return len(set(my_numbers).intersection(winning_numbers))


def part_2(cards: dict) -> int:
    ''' Solves for part 2.  '''
    return 0

if __name__ == "__main__":

    # puzzle_input = process_input('04/test_input.txt')
    puzzle_input = process_input('04/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))



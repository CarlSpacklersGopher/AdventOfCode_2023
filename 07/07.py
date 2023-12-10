card_values = {'A' : 14,
               'K' : 13,
               'Q' : 12,
               'J' : 11,
               'T' : 10,
               '9' : 9,
               '8' : 8,
               '7' : 7,
               '6' : 6,
               '5' : 5,
               '4' : 4,
               '3' : 3,
               '2' : 2
               }

def process_input(path: str) -> list[str]:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        return f.readlines()


def get_hand_score(hand:str) -> int:
    '''Returns 27 bit number containing score of a 5 card hand.  Bit def:
    Bit 26 (MSB) - 5 of a kind
    Bit 25 - 4 of a kind
    Bit 24 - Full House
    Bit 23 - 3 of a kind
    Bit 22 - 2 Pair
    Bit 21 - Pair
    Bit 20 - High Card
    ----
    Tiebreaker Begins
    Bit 16-19 - score of 1st card
    Bit 12-15 - score of 2nd card
    Bit 8-11 - score of 3rd card
    Bit 4-7 - score of 4th card
    Bit 0(LSB)-3 - score of 5th card

    Tiebreaker tacked onto end allows quick comparison per rules
    '''
    unique_count = len(set(hand))
    first_count = hand.count(hand[0])
    card_scores = [card_values[card] for card in hand]

    hand_score = 0
    # Hand Category
    if unique_count == 1:
        # 5 of a kind
        hand_score = 1 << 26
    elif unique_count == 2:
        if (first_count == 4) or (first_count == 1):
            hand_score = 1 << 25 # 4 of a kind
        else:
            hand_score = 1 << 24 # Full House
    elif unique_count == 3:
        check_count = first_count
        if check_count == 1: # Not useful for determining 3 of a kind vs 2 pair.
            check_count = hand.count(hand[1]) # Throw away the single, get something new
        if (check_count == 3) or (check_count == 1): # Second instance of 1, so know 3 of a kind
            hand_score = 1 << 23 # 3 of a kind
        else:
            hand_score = 1 << 22 # 2 pair
    elif unique_count == 4:
        hand_score = 1 << 21 # 1 pair
    else:
        hand_score = 1 << 20 # High Card

    # Tiebreaker
    tiebreaker = 0
    for idx, card_score in enumerate(card_scores):
        # Max score is 14, which is 4 bits.
        tiebreaker += card_score << (16 - 4*idx)

    return hand_score + tiebreaker

def part_1(puzzle_input: list[str]) -> int:
    ''' Solves for part 1. '''
    wagers = {}
    hands = []
    for line in puzzle_input:
        hand, wager = line.split()
        wagers[hand] = int(wager)
        hands.append(hand)

    hands.sort(key=get_hand_score)
    winnings = 0
    for idx, hand in enumerate(hands):
        # print('Strength: {}, Hand: {}, Bid: {}'.format(idx+1, hand, wagers[hand]))
        rank = idx + 1
        winnings += wagers[hand] * rank
    return winnings

def part_2(puzzle_input: list[str]) -> int:
    ''' Solves for part 2.  '''
    return 0


if __name__ == "__main__":
    # puzzle_input = process_input('07/test_input.txt')
    puzzle_input = process_input('07/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))
    '''
    # puzzle_input = process_input('07/input.txt')
    print("Part 2: " + str(part_2(puzzle_input)))
    '''
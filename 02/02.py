import re
from math import prod

MAX_CUBES = {'red': 12, 'green': 13, 'blue': 14}


class Game:
    ''' Represents a single game with multiple draws of different colored cubes'''
    # draws: list[dict[color,count]]
    def __init__(self, game:int, draws:list[dict]):
        self.game_number = game
        self.draws = draws

    def is_game_possible(self) -> bool:
        ''' Determines if any single draw exceeds max number of cubes.'''
        for draw in self.draws:
            for color, count in draw.items():
                if count > MAX_CUBES[color]:
                    return False
        return True

    def min_cubes(self) -> dict[str, int]:
        ''' Finds the minimum amount of cubes of each color to make the game possible.'''
        minimums = {}
        for draw in self.draws:
            for color, count in draw.items():
                if color not in minimums:
                    minimums[color] = count
                else:
                    if count > minimums[color]:
                        minimums[color] = count
        return minimums



def process_input(path: str) -> list:
    ''' Reads the puzzle input.'''
    with open(path, 'r') as f:
        games = []
        for line in f:
            game_string, draws_string = line.split(':')
            game_number = int(game_string.split()[-1])
            draws_str = draws_string.split(';')
            draws = []
            for draw_str in draws_str:
                draw_dict = {}
                counts = re.findall(r'\d+', draw_str)
                colors = re.findall(r'[a-z]+', draw_str.lower())
                for count, color in zip(counts, colors):
                    draw_dict[color] = int(count)
                draws.append(draw_dict)
            games.append(Game(game_number, draws))
        return games


def part_1(games: list[Game]) -> int:
    ''' Solves for part 1. '''
    possible_games = []
    for game in games:
        if game.is_game_possible():
            possible_games.append(game.game_number)
    return sum(possible_games)



def part_2(games: list[Game]) -> int:
    ''' Solves for part 2.  '''
    # Probably could solve this by calling is_game_possible to eliminate some of the checks.
    # But this is simpler :)
    game_powers = []
    for game in games:
        min_cubes = game.min_cubes()
        game_powers.append(prod(min_cubes.values()))
    return sum(game_powers)

if __name__ == "__main__":
    # puzzle_input = process_input('02/test_input.txt')
    puzzle_input = process_input('02/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))


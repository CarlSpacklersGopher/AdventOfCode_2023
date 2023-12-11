import sys
import os

def make_files(day_str:str):

    contents_dayx = '''

def process_input(path: str) -> list[str]:
    \'\'\' Reads the puzzle input. \'\'\'
    with open(path) as f:
        return f.readlines()

def part_1(puzzle_input:list[str]) -> int:
    \'\'\' Solves for Part 1. \'\'\'
    return 0

def part_2(puzzle_input:list[str]) -> int:
    \'\'\' Solves for Part 2. \'\'\'
    return 0

if __name__ == '__main__':
    puzzle_input = process_input('{day_str}}/test_input.txt')
    # puzzle_input = process_input('{day_str}}/input.txt')
    print("Part 1: " + str(part_1(puzzle_input)))

    print("Part 2: " + str(part_2(puzzle_input)))
    '''

    files = [('prompt.txt', ''),
             (day_str + '.py', contents_dayx),
             ('input.txt', ''),
             ('test_input.txt', '')]

    os.mkdir(day_str)
    for file_name, contents in files:
        with open (os.path.join(day_str, file_name), mode='w') as f:
            f.write(contents)

def make_prompt_readable(day:str, line_chars:int = 100):
    folder_name = day
    prompt_file = 'prompt.txt'
    prompt_path = os.path.join(folder_name, prompt_file)

    with open (prompt_path, mode='r+') as f:
        long_lines = f.readlines()
        broken_up_lines = []
        for long_line in long_lines:
            words = long_line.split(' ')
            this_line_words = []
            char_count = 0
            for word in words:
                char_count += len(word) + 1
                last_word = word.endswith('\n') # last words always have newline after
                if not last_word and (char_count < line_chars):
                    this_line_words.append(word)
                    char_count += 1 # account for space between words
                else:
                    if last_word:
                        this_line_words.append(word)
                        eol_append = ''
                    else:
                        eol_append = '\n'

                    short_line = ' '.join(this_line_words) + eol_append
                    broken_up_lines.append(short_line)
                    char_count = len(word)
                    this_line_words = [word] # overflow word onto next line
        f.seek(0)
        f.writelines(broken_up_lines)
        f.truncate()



if __name__ == '__main__':
    day_num_str = sys.argv[1]
    if len(sys.argv) == 2:
        make_files(day_num_str)
    else:
        make_prompt_readable(day_num_str)


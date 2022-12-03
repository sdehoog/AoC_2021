def char_score(char):
    if char == ')':
        return 3
    elif char == ']':
        return 57
    elif char == '}':
        return 1197
    elif char == '>':
        return 25137
    else:
        return -1

def line_score(line):
    score = 0
    score_dict = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4}
    for char in line:
        score = score * 5 + score_dict[char]

    return score

def flip_char(char):
    if char == '(':
        return ')'
    elif char == '[':
        return ']'
    elif char == '{':
        return '}'
    elif char == '<':
        return '>'
    else:
        return '!'
    
def matched_set(a,b):
    opens = ['(', '<', '{', '[']
    closes = [')', '>', '}', ']']

    if opens.index(a) == closes.index(b):
        return True
    else:
        return False

def syntax_score(file_path, bad_only):

    with open(file_path) as fin:
        chunk_lines = [x.strip() for x in fin.readlines()]

    matched = [([False] * len(row)) for row in chunk_lines]

    opens = ['(', '<', '{', '[']
    closes = [')', '>', '}', ']']

    bad_chars = []
    bad_lines = []

    for r_i in range(len(chunk_lines)):
        for c_i in range(len(chunk_lines[r_i])):
            char = chunk_lines[r_i][c_i]
            if char in closes:
                offset = 1
                try:
                    while matched[r_i][c_i - offset]:
                        if offset > c_i:
                            print('Offset greater than c_o')
                        else:
                            offset += 1
                except:
                    print(r_i,c_i, offset)

                if not matched_set(chunk_lines[r_i][c_i - offset], char):
                    bad_chars.append(char)
                    bad_lines.append(r_i)
                    break
                elif matched_set(chunk_lines[r_i][c_i - offset], char):
                    matched[r_i][c_i] = True
                    matched[r_i][c_i - offset] = True

    if bad_only:
        score = 0
        for char in bad_chars:
            score += char_score(char)
        return score

    bad_lines.reverse()
    for line in bad_lines:
        chunk_lines.pop(line)
        matched.pop(line)


    com_string = [[] for line in chunk_lines]
    
    for r_i in range(len(chunk_lines)):
        for c_i in range(len(chunk_lines[r_i])):
            if not matched[r_i][c_i]:
                com_string[r_i].append(flip_char(chunk_lines[r_i][c_i]))
        com_string[r_i].reverse()

    score = []
    
    for line in com_string:
        score.append(line_score(line))

    score.sort()
    half = (len(score) + 1) // 2
    
    return score[half - 1]
    
if __name__ == '__main__':

    assert syntax_score('test_input.txt', True) == 26397
    print(syntax_score('input.txt', True))

    assert syntax_score('test_input.txt', False) == 288957
    print(syntax_score('input.txt', False))

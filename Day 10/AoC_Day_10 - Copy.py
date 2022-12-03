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
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4}
    for char in line:
        score = score * 5 + score_dict[char]

    return score

    
def syntax_score(file_path, bad_only):

    with open(file_path) as fin:
        chunk_lines = [x.strip() for x in fin.readlines()]

    bad_score = 0
    a_score = []
    stack = []

    opens = ['(', '<', '{', '[']
    closes = [')', '>', '}', ']']

    for line in chunk_lines:
        stack.clear()
        for char in line:            
            if char in opens:
                stack.append(char)
            elif char in closes:
                if char == closes[opens.index(stack[-1])]:
                    stack.pop()
                else:
                    bad_score += char_score(char)
                    break
            else:
                print('uh oh')
        else:
            a_score.append(line_score(stack[::-1]))
            
    a_score.sort()
    
    if bad_only:
        return bad_score
    else:
        return a_score[len(a_score)//2]

def main():
    
    assert syntax_score('test_input.txt', True) == 26397
    print(syntax_score('input.txt', True))

    assert syntax_score('test_input.txt', False) == 288957
    print(syntax_score('input.txt', False))
    
if __name__ == '__main__':
    main()

OPENING = ['(', '[', '{', '<']
CLOSING = [')', ']', '}', '>']

data = [x.strip() for x in open('test_input.txt', 'r').readlines()]

score_list = []
for x in data:
    count = []
    score = 0
    error = False
    for y in x:
        if y in OPENING:
            count.append(y)
            print(count)
        elif y in CLOSING and y == CLOSING[OPENING.index(count[-1])]:
            count.pop()
            print(count)
        else:
            error = True
            break
    print(count[::-1])
    if len(count) and not error:
        for z in count[::-1]:
            score *= 5
            if z == '(':
                score += 1
            elif z == '[':
                score += 2
            elif z == '{':
                score += 3
            elif z == '<':
                score += 4
        score_list.append(score)
print(sorted(score_list)[int((len(score_list)-1)/2)])

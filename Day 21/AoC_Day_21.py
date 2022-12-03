from functools import cache
from time import perf_counter

moves = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            moves.append(sum([i,j,k]))

@cache
def quantom_roll(p1_pos, p2_pos, p1_score, p2_score, move, p1_roll):
    if p1_roll:        
        p1_pos = (p1_pos + move - 1) % 10 + 1
        p1_score += p1_pos
        if p1_score >= 21:
            return (1, 0)
        p1_roll = False
    else:
        p2_pos = (p2_pos + move - 1) % 10 + 1
        p2_score += p2_pos
        if p2_score >= 21:
            return (0, 1)
        p1_roll = True
                
    subgames = [quantom_roll(p1_pos, p2_pos, p1_score, p2_score, move, p1_roll) for move in moves]

    return sum([a for a, _ in subgames]), sum([b for _, b in subgames])
                    

def real_dirac_dice(file_path):
    
    with open(file_path) as fin:
        p1, p2 = [int(line.strip()[-1]) for line in fin.readlines()]

    p1_wins, p2_wins = quantom_roll(p1, p2, 0, -p2, 0, False)
    return max(p1_wins, p2_wins)

def dirac_dice(file_path, win_score):

    with open(file_path) as fin:
        p1, p2 = [int(line.strip()[-1]) for line in fin.readlines()]

    p1_score = 0
    p2_score = 0

    moves = [(i % 10) for i in range(16, 6, -1)]

    board = [i for i in range(1,11)]

    p1_pos = board.index(p1)
    p2_pos = board.index(p2)

    roll = 0

    while True:
        p1_pos += moves[roll % 10]
        p1_score += board[p1_pos % 10]
        roll += 1
        if p1_score >= win_score:
            break
        
        p2_pos += moves[roll % 10]
        p2_score += board[p2_pos % 10]
        roll += 1
        if p2_score >= win_score:
            break

    return roll * 3 *  min(p1_score, p2_score)

def main():

    assert dirac_dice('test_input.txt', 1000) == 739785
    print(dirac_dice('input.txt', 1000))

    start = perf_counter()
    assert real_dirac_dice('test_input.txt') == 444356092776315
    print('Test time:', perf_counter() - start)

    start = perf_counter()
    print(real_dirac_dice('input.txt'))
    print('Actual time:', perf_counter() - start)

    
if __name__ == '__main__':
    main()

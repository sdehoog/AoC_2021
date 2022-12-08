class Bingo_Board:
    
    
    
    
    
    def __init__(self, board_number):
        self.board = board_number
        self.marked = [[False]*5 for i in range(5)]
        self.bingo = False
        pass

    def print(self):
        for i in range(5):
            for j in range(5):
                if self.marked[i][j]:
                    print(str(self.board[i][j]).center(4,'*'), end = '')
                else:
                    print(str(self.board[i][j]).center(4), end = '')
            print('')
        print('')

    def check(self, number):

        for i in range(5):
            for j in range(5):
                if number == self.board[i][j]:
                    self.marked[i][j] = True

        self.bingo_check()

    def bingo_check(self):
        for i in range(5):
            if self.marked[i] == [True]*5:
                self.bingo = True
            elif self.marked[0][i] and self.marked[1][i] and self.marked[2][i] and self.marked[3][i] and self.marked[4][i]:
                self.bingo = True

## Board_1 = Bingo_Board([[0,0,0,0,0],
##                      [1,1,1,1,1],
##                      [2,2, 2, 2, 2],
##                      [3, 3, 3, 3, 3],
##                       [4, 4, 4, 4, 4]])
##
##Board_1 = Bingo_Board([[0,1,2,3,4],
##                       [0,1,2,3,4],
##                       [0,1,2,3,4],
##                       [0,1,2,3,4],
##                       [0,1,2,3,4]])
##Board_1.print()
##print(Board_1.bingo)
##
##Board_1.check(0)
##
##Board_1.print()
##
##Board_1.bingo_check()
##
##print(Board_1.bingo)

fin = open("""C:\\Users\\steve\\OneDrive\\Documents\\Advent of Code\\2021\\Day 04\\test_input.txt""")

numbers = []
numbers = fin.readline().strip().split(",")

Boards = []
while True:

    spam = fin.readline()
    if not spam:
        break
    Boards.append(Bingo_Board([fin.readline().strip().rsplit(),
            fin.readline().strip().rsplit(),
            fin.readline().strip().rsplit(),
            fin.readline().strip().rsplit(),
            fin.readline().strip().rsplit()]))
    for i in range(5):
        for j in range(5):
            Boards[-1].board[i][j] = int(Boards[-1].board[i][j])
            

fin.close()



for i in range(len(numbers)):
##    print("Number is " + str(numbers[i]))
    for j in range(len(Boards)):
        
        Boards[j].check(int(numbers[i]))
##        Boards[j].print()
##        print()
        if Boards[j].bingo == True:
            Boards[j].print()
            break

    else:
        continue
    break

board_sum = 0

winning_board = j
final_number = int(numbers[i])

for i in range(5):
    for j in range(5):
        if not Boards[winning_board].marked[i][j]:
            board_sum += Boards[winning_board].board[i][j]
            

print(final_number)    
print(board_sum)
print(final_number * board_sum)


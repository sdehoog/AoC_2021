from itertools import permutations

class SnailNumber:
    def __init__(self, snail_number, parent=None):
        self.parent = parent
        if isinstance(snail_number[0], int):
            self.left = snail_number[0]
        elif isinstance(snail_number[0], SnailNumber):
            self.left = snail_number[0]
            self.left.parent = self
        else:
            self.left = SnailNumber(snail_number[0], self)
        if type(snail_number[1]) is int:
            self.right = snail_number[1]
        elif type(snail_number[1]) is SnailNumber:
            self.right = snail_number[1]
            self.right.parent = self
        else:
            self.right = SnailNumber(snail_number[1], self)

    def __add__(self, other):
        return SnailNumber([self, other])

    def reduce(self):
        while self.explode() or self.split():
            # print(self)
            pass
        # while self.height() > 4 or self.double_digit():
        #     if self.height() > 4:
        #         self.explode()
        #         continue
        #     self.split()
        #     continue

    def explode(self):
        if self.depth() == 5:
            self.to_left(self.left, 'up')
            self.to_right(self.right, 'up')
            if self.parent.left == self:
                self.parent.left = 0
            else:
                self.parent.right = 0
            return True
        else:
            if isinstance(self.left, SnailNumber) and isinstance(self.right, SnailNumber):
                return self.left.explode() or self.right.explode()
            elif isinstance(self.left, SnailNumber):
                return self.left.explode()
            elif isinstance(self.right, SnailNumber):
                return self.right.explode()
        return False

    def to_left(self, value, direction):
        if direction == 'up':
            if self.parent is None:
                return
            if self.parent.left != self:
                if isinstance(self.parent.left, int):
                    self.parent.left += value
                else:
                    self.parent.left.to_left(value, 'down')
            else:
                self.parent.to_left(value, 'up')
        elif direction == 'down':
            if isinstance(self.right, int):
                self.right += value
            else:
                self.right.to_left(value, 'down')

    def to_right(self, value, direction):
        if direction == 'up':
            if self.parent is None:
                return
            if self.parent.right != self:
                if isinstance(self.parent.right, int):
                    self.parent.right += value
                else:
                    self.parent.right.to_right(value, 'down')
            else:
                self.parent.to_right(value, 'up')
        elif direction == 'down':
            if isinstance(self.left, int):
                self.left += value
            else:
                self.left.to_right(value, 'down')

    def split(self):
        if isinstance(self.left, int) and self.left > 9:
            self.left = SnailNumber([self.left // 2, self.left - self.left // 2], self)
            return True
        elif isinstance(self.left, int) and isinstance(self.right, int) and self.right > 9:
            self.right = SnailNumber([self.right // 2, self.right - self.right // 2], self)
            return True
        elif isinstance(self.left, SnailNumber) and self.left.double_digit():
            return self.left.split()
        elif isinstance(self.left, SnailNumber) and not(self.left.double_digit()) and isinstance(self.right, int) and self.right > 9:
            self.right = SnailNumber([self.right // 2, self.right - self.right // 2], self)
            return True
        elif isinstance(self.left, SnailNumber) and isinstance(self.right, SnailNumber):
            return self.left.split() or self.right.split()
        elif isinstance(self.left, SnailNumber):
            return self.left.split()
        elif isinstance(self.right, SnailNumber):
            return self.right.split()
        return False

    def depth(self):
        if self.parent is None:
            return 1
        else:
            return 1 + self.parent.depth()

    def magnitude(self):
        if isinstance(self.left, int):
            left_mag = self.left * 3
        else:
            left_mag = self.left.magnitude() * 3
        if isinstance(self.right, int):
            right_mag = self.right * 2
        else:
            right_mag = self.right.magnitude() * 2

        return left_mag + right_mag

    def __str__(self):
        return f'[{str(self.left)},{str(self.right)}]'

    def __repr__(self):
        return 'SnailNumber()'

    def height(self):
        if type(self.left) == int and type(self.right) == int:
            return 1
        else:
            return 1 + max(self.left.height() if isinstance(self.left, SnailNumber) else 0,
                           self.right.height() if isinstance(self.right, SnailNumber) else 0)

    # depreciated this class method in favor of returning true or false when splitting or exploding
    def double_digit(self):
        if isinstance(self.left, int) and self.left > 9:
            return True
        elif isinstance(self.right, int) and self.right > 9:
            return True
        elif isinstance(self.left, SnailNumber) and isinstance(self.right, SnailNumber):
            return self.left.double_digit() or self.right.double_digit()
        elif isinstance(self.left, SnailNumber):
            return self.left.double_digit()
        elif isinstance(self.right, SnailNumber):
            return self.right.double_digit()
        else:
            return False


def reduce_sn(sn_number: SnailNumber):
    while sn_number.explode() or sn_number.split():
        continue


def snail_homework(filepath, any_two=False):
    with open(filepath) as fin:
        snail_numbers = [eval(line) for line in fin.readlines()]

    if not any_two:
        first_sn = SnailNumber(snail_numbers[0])
        for sn in snail_numbers[1:]:
            next_sn = SnailNumber(sn)
            first_sn += next_sn
            first_sn.reduce()

        return first_sn.magnitude()
    else:
        mags = []
        for a, b in permutations(snail_numbers, 2):
            sn = SnailNumber(a) + SnailNumber(b)
            sn.reduce()
            mags.append(sn.magnitude())

        return max(mags)



def main():
    # sn1 = SnailNumber([[[[[9,8],1],2],3],4])
    # sn1.reduce()
    # print(sn1)

    # sn2 = SnailNumber([7,[6,[5,[4,[3,2]]]]])
    # sn2.reduce()
    # print(sn2)

    # sn3 = SnailNumber([[6,[5,[4,[3,2]]]],1])
    # sn3.reduce()
    # print(sn3)

    # sn4 = SnailNumber([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
    # sn4.reduce()
    # print(sn4)

    # sn5 = SnailNumber([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
    # sn5.reduce()
    # print(sn5)

    # sn6 = SnailNumber([[[[4,3],4],4],[7,[[8,4],9]]])
    # sn7 = SnailNumber([1,1])
    # sn8 = sn6 + sn7
    # sn8.reduce()
    # print(sn8)

    # sn9 = SnailNumber([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
    # sn9.explode()
    # print(sn9)

    #     test = '''[1,1]
    # [2,2]
    # [3,3]
    # [4,4]'''

    #     test = '''[1,1]
    # [2,2]
    # [3,3]
    # [4,4]
    # [5,5]'''

    # test = '''[1,1]
    # [2,2]
    # [3,3]
    # [4,4]
    # [5,5]
    # [6,6]'''
    #
    # lines = test.split('\n')
    # first_sn = SnailNumber(eval(lines[0]))
    # for line in lines[1:]:
    #     first_sn = first_sn + SnailNumber(eval(line))
    #     first_sn.reduce()
    # print(first_sn)

    # sn10 = SnailNumber([[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]])
    # sn11 = SnailNumber([7,[5,[[3,8],[1,4]]]])
    # sn12 = sn10 + sn11
    # sn12.reduce()
    # sn13 = SnailNumber([[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]])
    # print(sn12)
    # print(sn13)
    # assert str(sn12) == str(sn13)
    # print(snail_homework('test02'))
    # print(snail_homework('test01'))

    assert snail_homework('test01') == 4140
    print(snail_homework('input18'))

    assert snail_homework('test01', True) == 3993
    print(snail_homework('input18', True))


if __name__ == '__main__':
    main()

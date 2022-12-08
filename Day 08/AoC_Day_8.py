def find_code(sig_pat):
    code = ['z'] * 10
    six_len = []
    five_len = []
    for data in sig_pat:
        if len(data) == 2:
            code[1] = data
        elif len(data) == 3:
            code[7] = data
        elif len(data) == 4:
            code[4] = data
        elif len(data) == 7:
            code[8] = data
        elif len(data) == 5:
            five_len.append(data)
        elif len(data) == 6:
            six_len.append(data)
        else:
            print('Uh oh.')

    # the 4 has 2 extra values compared to the 1, this is used later
    four_extra = []
    for i in code[4]:
        if code[1].find(i) == -1:
            four_extra.append(i)

    # the top segment is the extra letter in the 7 compared to the 1
    for i in code[7]:
        if code[1].find(i) == -1:
             top = i
             break
            
    # the 8 has two extra values compared to the 4 plus the top, this is used later
    eight_extra = []
    four_top = ''.join([top,code[4]])
    for i in code[8]:
        if four_top.find(i) == -1:
            eight_extra.append(i)
            
    for num in six_len:
        for j in range(2):
            # if you can't find one of the 1 values in any of the 6 digit numbers,
            # it is the top left value, and the other is the bottom left
            if num.find(code[1][j]) == -1:
                top_right = code[1][j]
                bot_right = code[1][j - 1]
                
            # if you can't find one of the extra 8 values in any of the 6 digit numbers,
            # it is the it is the bottom left value, and the other is the bottom
            if num.find(eight_extra[j]) == -1:
                bot_left = eight_extra[j]
                bottom = eight_extra[j-1]

    for num in five_len:
        for j in range(2):
            # if you can't find one of the extra 4 values in any of the 5 length number,
            # it is the top left, and the other is the middle
            if num.find(four_extra[j]) == -1:
                top_left = four_extra[j]
                middle = four_extra[j - 1]
                break
        else:
            continue
        break

    code[2] = ''.join(sorted(''.join([top, top_right, middle, bot_left, bottom])))
    code[3] = ''.join(sorted(''.join([top, top_right, middle, bot_right, bottom])))
    code[5] = ''.join(sorted(''.join([top, top_left, middle, bot_right, bottom])))
    code[6] = ''.join(sorted(''.join([top, top_left, middle, bot_right, bottom, bot_left])))
    code[9] = ''.join(sorted(''.join([top, top_left, middle, bot_right, bottom, top_right])))
    code[0] = ''.join(sorted(''.join([top, top_left, bot_left, bot_right, bottom, top_right])))

    return code

def find_value(out_val, code):

    return int(''.join([str(code.index(val)) for val in out_val]))

                        
def seg_decode(filepath, count_only):

    out_val = []
    sig_pat = []
    with open(filepath) as fin:
        for line in fin.readlines():
            out_val.append(0)
            sig_pat.append(0)
            sig_pat[-1], out_val[-1] = [data.strip().split(' ') for data in line.split('|')]

    for i in range(len(sig_pat)):
        for j in range(len(sig_pat[i])):
            sig_pat[i][j] = ''.join(sorted(sig_pat[i][j]))
        for j in range(len(out_val[i])):
            out_val[i][j] = ''.join(sorted(out_val[i][j]))
            
    if count_only:
        u_count = 0
        for row in out_val:
            for data in row:
                if len(data) == 2 or len(data) == 3 or len(data) == 4 or len(data) == 7:
                    u_count += 1

        return u_count

    else:
        out_sum = 0
        for row in range(len(sig_pat)):
            out_sum += find_value(out_val[row], find_code(sig_pat[row]))
        return out_sum

if __name__ == '__main__':

    assert seg_decode('test_input.txt',True) == 26
    print(seg_decode('input.txt', True))

    assert seg_decode('test_input.txt',False) == 61229
    print(seg_decode('input.txt', False))

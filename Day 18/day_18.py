def main():
    def magnitude(sn):
        pass


    def explode(sn_to_explode, start):
        pass


    def sn_reduce(sn_to_reduce):
        level = 0
        for i, char in enumerate(sn_to_reduce):
            if char == '[':
                level += 1
                if level == 5:
                    exploded_sn = explode(sn_to_reduce, i)
                    return sn_reduce(exploded_sn)


    sns = ['[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]']
    base_sn = sns[0]
    for sn in sns[1:]:
        base_sn = '[' + base_sn + ',' + sn + ']'
        base_sn = sn_reduce(base_sn)

    mag = magnitude(base_sn)
    print(mag)



if __name__ == '__main__':
    main()
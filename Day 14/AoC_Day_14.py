from collections import Counter

def poly(file_name, steps):
    with open(file_name) as fin:
        start, rules = fin.read().strip().split('\n\n')

    rules_dict = dict()
    for rule in rules.splitlines():
         rules_dict[rule.split(' -> ')[0]] = rule.split(' -> ')[1]

    chain = {key: 0 for key in rules_dict}

    grow = {key: 0 for key in chain}
    
    elements = Counter(rules_dict.values())    
    elements = {key: 0 for key in elements}

    for i in list(start):
        elements[i] += 1
    
    for i in range(len(start) - 1):
        chain[start[i:i+2]] += 1

    for step in range(steps):
        for key, val in chain.items():
            if val > 0:
                splice = rules_dict[key]
                elements[splice] += val
                first = ''.join([key[0],splice])
                second = ''.join([splice,key[1]])
                
                grow[first] += val
                grow[second] += val
                grow[key] -= val
                
        for key in chain:
            chain[key] += grow[key]
            
        grow = {key: 0 for key in chain}

    return max(elements.values()) - min(elements.values())

def main():

    assert poly('test_input.txt', 10) == 1588
    print(poly('input.txt', 10))

    assert poly('test_input.txt', 40) == 2188189693529
    print(poly('input.txt', 40))

if __name__ == '__main__':
    main()

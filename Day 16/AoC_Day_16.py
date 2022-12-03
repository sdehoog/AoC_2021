class Packet:

    def __init__(self, binary):
        self.binary = binary
        self.is_parsed = False

    def parse(self):
        self.is_parsed = True
        self.version = int(self.binary[:3],2)
        self.type_ID = int(self.binary[3:6],2)

        if self.type_ID == 4:
            self.kind = 'literal'
            return self._parse_literal(self.binary[6:])
        else:
            self.kind = 'operator'
            self.children = []
            self.length_type = int(self.binary[6])
            if self.length_type == 0:
                self.length = int(self.binary[7:22],2)
                new_packet = Packet(self.binary[22:])
                self.children.append(new_packet)
                remainder = new_packet.parse()
                while len(self.binary) -22 - len(remainder) < self.length:
                    new_packet = Packet(remainder)
                    self.children.append(new_packet)
                    remainder = new_packet.parse()
                return remainder
            elif self.length_type == 1:
                self.n_children = int(self.binary[7:18],2)
                new_packet = Packet(self.binary[18:])
                self.children.append(new_packet)
                remainder = new_packet.parse()
                for _ in range(self.n_children - 1):
                    new_packet = Packet(remainder)
                    self.children.append(new_packet)
                    remainder = new_packet.parse()
                return remainder

    def _parse_literal(self, binary):
        i = 0
        value_text = ''
        while True:
            seg = binary[i:i + 5]
            value_text += seg[1:5]
            i += 5
            if seg[0] == '0':
                break

        self.value = int(value_text, 2)
        return binary[i:]

    def version_sum(self):
        if not hasattr(self, 'kind'):
            return none

        if self.kind == 'literal':
            return self.version
        return self.version + sum(c.version_sum() for c in self.children)

    def evaluate(self):
        if not self.is_parsed:
            return None
        
        if self.kind =='literal':
            return self.value

        if self.type_ID == 0:
            return sum(c.evaluate() for c in self.children)

        if self.type_ID == 1:
            p = 1
            for c in self.children:
                p *= c.evaluate()
            return p

        if self.type_ID == 2:
            return min(c.evaluate() for c in self.children)

        if self.type_ID == 3:
            return max(c.evaluate() for c in self.children)

        if self.type_ID == 5:
            return int(self.children[0].evaluate() > self.children[1].evaluate())

        if self.type_ID == 6:
            return int(self.children[0].evaluate() < self.children[1].evaluate())

        if self.type_ID == 7:
            return int(self.children[0].evaluate() == self.children[1].evaluate())

        
        
    
def hex_to_bin(in_stream):
    o_stream = ''
    hex_table = '''0 = 0000
                    1 = 0001
                    2 = 0010
                    3 = 0011
                    4 = 0100
                    5 = 0101
                    6 = 0110
                    7 = 0111
                    8 = 1000
                    9 = 1001
                    A = 1010
                    B = 1011
                    C = 1100
                    D = 1101
                    E = 1110
                    F = 1111'''

    hex_dict = {}
    for line in hex_table.split('\n'):
        hex_dict[line.split(' = ')[0].strip()] = line.split(' = ')[1].strip()
        
    for i in in_stream:
        o_stream += hex_dict[i]

    return o_stream

def parse_packet(file_path, ver_sum_only=True):

    with open(file_path) as fin:
        hex_stream = fin.readline().strip()

    bin_stream = hex_to_bin(hex_stream)

    p = Packet(bin_stream)
    p.parse()

    if ver_sum_only:
        return p.version_sum()
    else:
        return p.evaluate()
    

def main():
    
    assert parse_packet('test_input5.txt') == 6
    assert parse_packet('test_input1.txt') == 16
    assert parse_packet('test_input2.txt') == 12
    assert parse_packet('test_input3.txt') == 23
    assert parse_packet('test_input4.txt') == 31
    print(parse_packet('input.txt'))

    assert parse_packet('test_input6.txt', False) == 3
    assert parse_packet('test_input7.txt', False) == 54
    assert parse_packet('test_input8.txt', False) == 7
    assert parse_packet('test_input9.txt', False) == 9
    assert parse_packet('test_input10.txt', False) == 1
    assert parse_packet('test_input11.txt', False) == 0
    assert parse_packet('test_input12.txt', False) == 0
    assert parse_packet('test_input13.txt', False) == 1
    print(parse_packet('input.txt', False))
    

if __name__ == '__main__':
    main()

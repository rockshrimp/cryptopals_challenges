from hex_to_base64 import hex_to_b64


def fixed_xor(s1, s2):
    return "".join([hex(int(x, 16) ^ int(y, 16))[2:] for (x, y) in zip(s1, s2)])


if __name__ == '__main__':
    s_1 = '1c0111001f010100061a024b53535009181c'
    s_2 = '686974207468652062756c6c277320657965'

    assert(fixed_xor(s_1, s_2) == '746865206b696420646f6e277420706c6179')

from fixed_xor import fixed_xor
from langdetect import detect


def single_byte_xor(char, hex_s):
    # For a hex string a byte is 2 characters
    n_bytes = len(hex_s) // 2
    return fixed_xor(hex_s, n_bytes * char)


def is_english(s):
    return detect(guess) == 'en'


if __name__ == '__main__':
    cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

    for i in range(128):
        c = hex(i)[2:].zfill(2)
        try:
            guess = bytearray.fromhex(single_byte_xor(c, cipher)).decode()
            if is_english(guess):
                print(guess)
        except:
            pass

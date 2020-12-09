from fixed_xor import fixed_xor
from langdetect import detect_langs

valid_char_values = range(32, 129)


def single_byte_xor(char, hex_string):
    if len(hex_string) % 2 == 1:
        raise ValueError('cipher length is not a multiple of 2')
    # For a hex string a byte is 2 characters
    n_bytes = len(hex_string) // 2
    return fixed_xor(hex_string, n_bytes * char)


def is_english(s):
    language, score = str(detect_langs(s)[0]).split(':')

    if language == 'en' and float(score) > 0.9:
        for char in s:
            # If we found non standars characters
            if ord(char) not in valid_char_values:
                return False
        return True
    else:
        return False


def guess_single_char_xor(s):
    possible_guesses = []
    for i in valid_char_values:
        c = hex(i)[2:].zfill(2)
        try:
            guess = bytearray.fromhex(single_byte_xor(c, s)).decode()
            if is_english(guess):
                possible_guesses.append(guess)
        # If there is a unicode decode error it means that the guess contains characters
        # that couldn't be decoded, so it's surely not the right guess
        except UnicodeDecodeError as e:
            pass
        except ValueError as e:
            raise e

    return possible_guesses


if __name__ == '__main__':
    cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    possibles_guesses = guess_single_char_xor(cipher)
    for guess in possibles_guesses:
        print(guess)

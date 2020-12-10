from fixed_xor import fixed_xor
from collections import Counter


def single_byte_xor(value, hex_string):
    s = bytes.fromhex(hex_string)
    return ''.join([chr(value ^ byte) for byte in s])


def get_english_score(s):
    # English character frequencies
    eng_letter_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .18288
    }
    s_frequencies = Counter(s)

    score = 0
    for letter in s_frequencies:
        score += abs(s_frequencies[letter] / len(s) - eng_letter_frequencies.get(letter, 0))
    return score


def guess_single_char_xor(s):
    possible_guesses = []
    for i in range(256):
        guess = single_byte_xor(i, s)
        score = get_english_score(guess)
        guess_entry = {'guess': guess,
                       'score': score}
        possible_guesses.append(guess_entry)

    return sorted(possible_guesses, key=lambda x: x['score'])[0]


if __name__ == '__main__':
    cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(guess_single_char_xor(cipher))

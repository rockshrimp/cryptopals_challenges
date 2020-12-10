from single_byte_xor import guess_single_char_xor, get_english_score

if __name__ == '__main__':
    with open('4.txt', 'r') as f:
        lines = f.read().split('\n')

        guesses = []
        for line in lines:
            guesses.append(guess_single_char_xor(line))
        print(sorted(guesses, key=lambda x: x['score'])[0])

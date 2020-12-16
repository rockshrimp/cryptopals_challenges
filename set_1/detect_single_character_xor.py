from single_byte_xor import guess_single_char_xor

if __name__ == '__main__':
    with open('4.txt', 'r') as f:
        lines = f.read().split('\n')

        guesses = []
        for line in lines:
            guesses.append(guess_single_char_xor(bytes.fromhex(line)))

        print(sorted(guesses, key=lambda x: x['score'])[0])

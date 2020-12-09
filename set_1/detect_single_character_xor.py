from single_byte_xor import guess_single_char_xor

if __name__ == '__main__':
    with open('4.txt', 'r') as f:
        lines = f.read().split('\n')
        for line in lines:
            guesses = guess_single_char_xor(line)
            if len(guesses) > 0:
                print(guesses)

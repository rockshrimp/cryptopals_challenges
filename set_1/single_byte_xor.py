from fixed_xor import fixed_xor
from langdetect import detect
if __name__ == '__main__':
    cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    n = len(cipher) // 2

    for i in range(128):
        c = hex(i)[2:].zfill(2)

        try:
            guess = bytearray.fromhex(fixed_xor(cipher, n*c)).decode()
            if detect(guess) == 'en':
                print(guess)
        except:
            pass

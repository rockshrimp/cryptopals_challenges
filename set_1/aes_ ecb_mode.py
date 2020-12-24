from Crypto.Cipher import AES
from base64 import b64decode


def decrypt_aes_cbc(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    pt = cipher.decrypt(ciphertext)
    return pt


if __name__ == '__main__':
    key = b'YELLOW SUBMARINE'
    with open('7.txt', 'rb') as f:
        ciphertext = b64decode(f.read())

    print(decrypt_aes_cbc(ciphertext, key))
    # b"I'm back and I'm ringin' the bell \nA rockin' on the mike while the fly girls yell ...
from base64 import b64encode


def hex_to_b64(string):
    return b64encode(bytes.fromhex(string)).decode()


if __name__ == '__main__':
    s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    r = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    print(hex_to_b64(s) == r)

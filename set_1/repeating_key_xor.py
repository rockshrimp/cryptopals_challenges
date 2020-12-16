def repeating_key_xor(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])


if __name__ == '__main__':
    message = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    solution = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272' \
               'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'
    key = b'ICE'
    assert (repeating_key_xor(message, key).hex() == solution)

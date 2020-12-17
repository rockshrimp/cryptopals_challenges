from base64 import b64decode
from single_byte_xor import guess_single_char_xor
from repeating_key_xor import repeating_key_xor


def str_to_binary(str):
    return ''.join([bin(ord(c))[2:].zfill(8) for c in str])


def bytes_to_binary(str):
    return ''.join([bin(c)[2:].zfill(8) for c in str])


def get_hamming_distance(str_1, str_2):
    str_1_bin = bytes_to_binary(str_1)
    str_2_bin = bytes_to_binary(str_2)

    return sum([str_1_bin[i] != str_2_bin[i] for i in range(min(len(str_1_bin), len(str_2_bin)))])


def get_distance_dic(key_size_range, cipher):
    distance_dic = {}
    for key_size in key_size_range:
        cipher_blocs = [cipher_bytes[i:i + key_size] for i in range(0, len(cipher), key_size)]

        distance = 0
        for i in range(0, len(cipher_blocs) - 1, 2):
            distance += get_hamming_distance(cipher_blocs[i], cipher_blocs[i + 1])

        distance_dic[key_size] = distance
    return distance_dic


def get_lowest_distances(n, dic):
    """
    :param n: number of element to be returned
    :param dic: dictionary containing the distances
    :return: the n entries (keysize: distance) with lowest distances
    """
    sorted_distance_dict = dict(sorted(dic.items(), key=lambda item: item[1]))
    return {k: sorted_distance_dict[k] for k in list(sorted_distance_dict)[:n]}


def group_bytes_per_index(key_size, cipher_bytes):
    """
    # groups all bytes by their index in the blocs of size key_size, e.g :
    # bytes_per_index[0] = (cipher_blocs[0][0], cipher_blocs[1][0], cipher_blocs[2][0], ...)
    # bytes_per_index[1] = (cipher_blocs[0][1], cipher_blocs[1][1], cipher_blocs[2][1], ...)
    """

    for i in range(key_size):
        yield cipher_bytes[i::key_size]


if __name__ == '__main__':
    s_1 = b'this is a test'
    s_2 = b'wokka wokka!!!'

    assert (get_hamming_distance(s_1, s_2) == 37)

    key_size_range = range(2, 40)
    nb_of_key_sizes_to_try = 3

    with open('6.txt', 'rb') as f:
        cipher = f.read()
    cipher_bytes = b64decode(cipher)

    # Generate a dictionary that contains the Hamming distance between blocks of size key_size
    distance_by_key_size_dict = get_distance_dic(key_size_range, cipher_bytes)
    lowest_distances_by_key_size = get_lowest_distances(nb_of_key_sizes_to_try, distance_by_key_size_dict)

    possible_keys = []
    for key_size in lowest_distances_by_key_size:
        bytes_per_index = group_bytes_per_index(key_size, cipher_bytes)

        key_guess = bytearray()
        # Solve the single byte xor for each group of bytes
        for byte_group in bytes_per_index:
            guess_value = guess_single_char_xor(byte_group)
            key_guess.append(guess_value['value'])
        possible_keys.append(key_guess)

    # We found that the most probable key is 'Terminator X: Bring the noise'
    key = possible_keys[0]
    clear_text = repeating_key_xor(cipher_bytes, key)

    # Gives us the lyrics of Vanilla Ice - Play That Funky Music
    print(''.join([chr(c) for c in clear_text]))

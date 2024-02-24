from bitarray import bitarray

# simplified version without complete f, instead of it is used xor 
class SimpleDES:
    _init_replace_table = (
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    )
    _end_replace_table = (
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    )
    
    keys = []

    @staticmethod
    def encode(string: str, key: str) -> str:
        result = ''
        blocks = SimpleDES._divide_into_blocks(string)

        for block in blocks:
            block_result = SimpleDES._init_replace_block(block)
            block_result = SimpleDES._iteration(block_result, key)
            block_result = SimpleDES._end_replace_block(block_result)

            result += str(hex(int(block_result.encode(), 2)))

        return result

    @staticmethod
    def decode(string: str, key: str) -> str:
        result = []
        blocks = SimpleDES._merge_blocks(string)

        for block in blocks:
            block_result = SimpleDES._init_replace_block(block)
            block_result = SimpleDES._iteration(block_result, key, decode=True)
            block_result = SimpleDES._end_replace_block(block_result)

            for i in range(0, len(block_result), 8):
                result.append(block_result[i: i + 8])

        return SimpleDES._bits_to_str(result)

    @staticmethod
    def _str_to_bits(string: str) -> str:
        return bitarray(
            ''.join([bin(int('1' + hex(c)[2:], 16))[3:]
                     for c in string.encode('utf-8')])).to01()
    
    @staticmethod
    def _bits_to_str(s: list) -> str:
        return ''.join([chr(i) for i in [int(b, 2) for b in s]])
    
    @staticmethod
    def _divide_into_blocks(string: str) -> list:
        result = []
        bit_string = SimpleDES._str_to_bits(string)

        if len(bit_string) % 64 != 0:
            for i in range(64 - len(bit_string) % 64):
                bit_string += '0'

        for i in range(len(bit_string) // 64):
            result.append(bit_string[i * 64: i * 64 + 64])

        return result
    
    @staticmethod
    def _merge_blocks(string: str) -> list:
        result = []

        input_list = string.split("0x")[1:]
        int_list = [int("0x" + i, 16) for i in input_list]

        for i in int_list:
            bin_data = str(bin(i))[2:]

            while len(bin_data) < 64:
                bin_data = '0' + bin_data
                
            result.append(bin_data)

        return result
    
    @staticmethod
    def _init_replace_block(block: str) -> str:
        return SimpleDES._replace_block(block, SimpleDES._init_replace_table)
    
    @staticmethod
    def _end_replace_block(block: str) -> str:
        return SimpleDES._replace_block(block, SimpleDES._end_replace_table)
    
    @staticmethod
    def _replace_block(block: str, table: tuple) -> str:
        result = ''
        for i in table:
            result += block[i - 1]
        return result
    
    @staticmethod
    def _key_conversion(key: str):
        key = SimpleDES._str_to_bits(key)

        while len(key) < 64:
            key += '0'

        first_key = key[:64]

        key_replace_table = (
            57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
        )
        
        return SimpleDES._replace_block(first_key, key_replace_table)

    @staticmethod
    def _spin_key(key: str):
        kc = SimpleDES._key_conversion(key)
        first, second = kc[0: 28], kc[28: 56]
        spin_table = (1, 2, 4, 6, 8, 10, 12, 14, 15, 17, 19, 21, 23, 25, 27, 28)

        for i in range(1, 17):
            first_after_spin = first[spin_table[i - 1]:] + first[:spin_table[i - 1]]
            second_after_spin = second[spin_table[i - 1]:] + second[:spin_table[i - 1]]
            yield first_after_spin + second_after_spin

    @staticmethod
    def _key_selection_replacement(key: str):
        SimpleDES.keys = []
        key_select_table = (
            14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
        )
        for child_key56 in SimpleDES._spin_key(key):
            SimpleDES.keys.append(SimpleDES._replace_block(child_key56, key_select_table))

    @staticmethod
    def _xor(a: str, b: str) -> str:
        result = ''
        size = len(a) if len(a) < len(a) else len(b)
        for i in range(size):
            result += '0' if a[i] == b[i] else '1'
        return result

    @staticmethod
    def _iteration(block: str, key: str, decode=False) -> str:
        SimpleDES._key_selection_replacement(key)

        for i in range(16):
            left, right = block[:32], block[32:]
            next_left = right

            if decode:
                f_result = SimpleDES._xor(right, SimpleDES.keys[16 - i - 1][:32])
            else:
                f_result = SimpleDES._xor(right, SimpleDES.keys[i][:32])

            right = SimpleDES._xor(left, f_result)
            block = next_left + right

        return block[32:] + block[:32]
        

def encrypt_des(data, key: str): 
    if isinstance(data, str):
        encrypted_value = SimpleDES.encode(data, key)
        return encrypted_value

    encrypted_dict = {}
    for k, v in data.items():
        encrypted_value = SimpleDES.encode(v, key)
        encrypted_dict[k] = encrypted_value
    return encrypted_dict

def decrypt_des(data, key: str):
    if isinstance(data, str):
        decrypted_value = SimpleDES.decode(data, key)
        return decrypted_value.replace('\x00', '')

    decrypted_dict = {}
    for k, v in data.items():
        decrypted_value = SimpleDES.decode(v, key)
        decrypted_dict[k] = decrypted_value

    cleaned_data = {key: value.replace('\x00', '') for key, value in decrypted_dict.items()}
    
    return cleaned_data

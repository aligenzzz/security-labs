from caesar import encoder_caesar, decoder_caesar
from constants import ALPHABET
import math
import re

def encoder_vigener(str: str, key: str):
    return vigener(str, key, 'encoder')

def decoder_vigener(str: str, key: str):
    return vigener(str, key, 'decoder')

def vigener(str: str, key: str, option: str):
    pattern = re.compile(r'^[a-zA-Z]+$')
    if not bool(pattern.match(key)):
        raise Exception('Invalid key form!')
    
    latin_letters = re.sub(r'[^a-zA-Z]', '', str)
      
    result = ''
    n = len(latin_letters)
    repeated_key = (key * math.ceil(n / len(key)))[:n]  

    k = 0
    for s in str:
        if s.lower() not in ALPHABET:
            result += s
            continue

        if option == 'encoder':
            if s.isupper():
                result += encoder_caesar(repeated_key[k].upper(), ALPHABET[s.lower()])
            else:
                result += encoder_caesar(repeated_key[k].lower(), ALPHABET[s.lower()])
        elif option == 'decoder':
            result += decoder_caesar(s, ALPHABET[repeated_key[k].lower()])
        else:
            raise Exception('Invalid option!')
        
        k += 1

    return result

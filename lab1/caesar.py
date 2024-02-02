from constants import ALPHABET

def encoder_caesar(str: str, k: int):
    return caesar(str, k, 'encoder')

def decoder_caesar(str: str, k: int):
    return caesar(str, k, 'decoder')

def caesar(str: str, k: int, option: str):
    if k < 0:
        raise Exception('Negative key value!')
    
    result = ''
    n =  len(ALPHABET)
    INVERTED = {v: k for k, v in ALPHABET.items()}

    for s in str:
        if s.lower() not in ALPHABET:
            result += s
        else:
            if option == 'encoder':
                x = INVERTED[(ALPHABET[s.lower()] + k) % n]
            elif option == 'decoder':
                x = INVERTED[(ALPHABET[s.lower()] - k + n) % n]
            else:
                raise Exception('Invalid option!')
            
            if s.isupper():
                result += x.capitalize()
            else:
                result += x

    return result

from caesar import encoder_caesar, decoder_caesar
from vigener import encoder_vigener, decoder_vigener
from constants import FILEPATH

if __name__ == '__main__':
    try:
        with open(FILEPATH, 'r') as file:
            content = file.read()
            
        print('1 Caesar encode')
        print('2 Caesar decode')
        print('3 Vigener encode')
        print('4 Vigener decode')

        choice = input('Enter choice: ')

        if choice == '1':
            key = int(input('Input key: '))
            result = encoder_caesar(content, key)
        elif choice == '2':
            key = int(input('Input key: '))
            result = decoder_caesar(content, key)
        elif choice == '3':
            key = input('Input key: ')
            result = encoder_vigener(content, key)
        elif choice == '4':
            key = input('Input key: ')
            result = decoder_vigener(content, key)
        else:
            raise Exception('Invalid choice!')
        
        with open(FILEPATH, 'w') as file:
            file.write(result)
            
    except FileNotFoundError:
        print(f'This file doesn\'t exist!')
    except Exception as e:
        print(f'{e}')
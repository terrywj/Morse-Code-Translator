# 1. input string
# 2. look up from dic
# 3. return Morse Code
# 4. Need to consider everything that is not A-Z or 0-9. e.g. symbol .,?, space

morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',

    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',

    ' ': '/',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    '¿': '..-.-',
    '¡': '--...-',

}


def encode(input_code):
    output_string = ''
    for letter in input_code:
        if letter in morse_code_dict.keys():
            output_string += morse_code_dict[letter]
            output_string += ' '
        else:
            output_string += letter
            output_string += ' '
    return output_string[:-1]


def decode(input_code):
    output_string = ''
    flip_morse_dict = {v: k for k, v in morse_code_dict.items()}
    input_code += ' '
    word = ''
    for char in input_code:
        if char != ' ':
            word += char
        elif word in flip_morse_dict.keys():
            output_string += flip_morse_dict[word]
            word = ''
        else:
            output_string += word
            word = ''
    return output_string


def engine(engine_mode, input_code):
    if engine_mode == 'E':
        print(f'Your output is:\n{encode(input_string)}')
    else:
        print(f'Your output is:\n{decode(input_string)}')


engine_on = True
while engine_on:
    mode = input("Do you want to encode text or decode morse code? Enter e or d: ").upper()
    if mode not in ['E', 'D']:
        continue
    input_string = input("Please enter your sentence.\n").upper()
    print(f"Your input is:\n{input_string}")
    engine(mode, input_string)
    next_engine = input("Do you want to continue next? Y/N: ").upper()
    if next_engine not in ['Y', 'YES']:
        engine_on = False
        print("Thank you for using our translator!")





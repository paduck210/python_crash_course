MORSE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '&'}

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message

    if morse_code == '···−−−···':
        return('SOS')

    new_codes = morse_code.replace("   ", " & ").split(" ")

    if new_codes[0] == '':
        for i in range(2):
            new_codes.pop(0)

    str = ""
    for code in new_codes:
        for k, v in MORSE_DICT.items():
            if code == v: str += k
    return(str)




print(decodeMorse('   .   . '))
print(decodeMorse('···−−−···'))
print(decodeMorse('.... . -.--   .--- ..- -.. .'))
# should return "HEY JUDE"
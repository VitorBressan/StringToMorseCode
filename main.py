import os

# Dictionary mapping each character to its corresponding Morse code
MORSE_CODE_DICT: dict[str, str] = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.",
    "$": "...-..-", "@": ".--.-.", " ": "/"
}

# String to be translated to Morse code
text_to_translate: str = str(input("Texto a ser traduzido:"))

# Converts each character of text_to_translate into Morse code
morse_code_text: str = ""
for char in text_to_translate:
    char = char.upper()
    if char in MORSE_CODE_DICT:
        morse_code_text += MORSE_CODE_DICT[char] + " "

os.system('clear || cls')
print(f"Original text: {text_to_translate}\nMorse code: {morse_code_text}")
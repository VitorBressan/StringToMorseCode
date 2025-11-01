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

# Converts each character of a text into Morse code
def convert_to_morse(text: str):
    morse_code_text: str = ""
    for char in text_to_translate:
        char = char.upper()
        if char in MORSE_CODE_DICT:
            morse_code_text += MORSE_CODE_DICT[char] + " "
    return morse_code_text

while True:

    # String to be translated to Morse code
    text_to_translate: str = str(input('Text to be translated ("Exit to leave"):'))
    os.system('clear || cls')

    # Exit the aplication if the users type "Exit"
    if text_to_translate == "Exit":
        print("Thank you for using this program!")
        break

    # Prints the translation
    print(f"Original text: {text_to_translate}\nMorse code: {convert_to_morse(text_to_translate)}")

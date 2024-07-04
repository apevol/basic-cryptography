# dictionary to store all morse code values for each character
MORSE_VALUES: dict = {"A": ".-",
                      "B": "-...",
                      "C": "-.-.",
                      "D": "-..",
                      "E": ".",
                      "F": "..-.",
                      "G": "--.",
                      "H": "....",
                      "I": "..",
                      "J": ",----",
                      "K": "-.-",
                      "L": ".-..",
                      "M": "--",
                      "N": "-.",
                      "O": "---",
                      "P": ".--.",
                      "Q": "--.-",
                      "R": ".-.",
                      "S": "...",
                      "T": "-",
                      "U": "..-",
                      "V": "...-",
                      "W": ".--",
                      "X": "-..-",
                      "Y": "-.--",
                      "Z": "--..",
                      "0": "-----",
                      "1": ".----",
                      "2": "..---",
                      "3": "...--",
                      "4": "....-",
                      "5": ".....",
                      "6": "-....",
                      "7": "--...",
                      "8": "---..",
                      "9": "----."
                      }


# encodes the string into morse code
def encode(message: str) -> str:
    message = message.upper()
    encrypted_message: str = ""
    for char in message:
        if char == " ":
            encrypted_message += "/ "
        else:
            # gets the morse code for the current character
            encoded_value: str = MORSE_VALUES.get(char) + " "
            encrypted_message += encoded_value
    return encrypted_message


# decodes a morse code string into plain text
def decode(message: str) -> str:
    decrypted_message: str = ""
    characters: list[str] = message.split(" ")
    for char in characters:
        if char == "/":
            decrypted_message += " "
        else:
            # separates keys and values in two lists, finds index of char and finds the key relating to that index
            plaintext_char = list(MORSE_VALUES.keys())[list(MORSE_VALUES.values()).index(char)]
            decrypted_message += plaintext_char
    return decrypted_message


def get_input() -> str:
    while True:
        try:
            # asks for a direction (encode or decode)
            direction: str = input("Encode or decode ( e or d): ").lower()
            match direction:
                case "e":
                    # asks for message and inputs into encode function
                    message: str = str(input("Message: "))
                    result: str = encode(message)
                    break
                case "d":
                    # asks for message and inputs into decode function
                    message: str = str(input("Message: "))
                    result: str = decode(message)
                    break
                case _:
                    raise ValueError
        except ValueError:
            print("[!] Incorrect value entered...")
    return result

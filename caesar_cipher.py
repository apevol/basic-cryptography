import string

LOWERCASE: str = string.ascii_lowercase
UPPERCASE: str = string.ascii_uppercase


# encode the message with a caesar cipher using a given shift value
def encode(message: str, shift: int) -> str:
    encrypted_message: str = ""
    for char in message:
        # check if char is a non-letter character
        if not char.isalpha():
            encrypted_message += char
        # check if char is uppercase
        elif char.isupper():
            # find the index of the char in the alphabet
            index: int = UPPERCASE.index(char)
            # find the index of the encrypted char (index + shift)
            # mod 26 so that the new_index does not exceed 25
            new_index: int = (index + shift) % 26
            encrypted_message += UPPERCASE[new_index]
        # check if char is lowercase
        elif char.islower():
            index: int = LOWERCASE.index(char)
            new_index: int = (index + shift) % 26
            encrypted_message += LOWERCASE[new_index]
    return encrypted_message


# decode the message with a caesar cipher using a given shift value
def decode(message: str, shift: int) -> str:
    decrypted_message: str = ""
    for char in message:
        # check if char is a non-letter character
        if not char.isalpha():
            decrypted_message += char
        # check if char is uppercase
        elif char.isupper():
            # find the index of the char in the alphabet
            index: int = UPPERCASE.index(char)
            # find the index of the decrypted char (index - shift)
            # mod 26 so that the new_index does not exceed 25
            new_index: int = (index - shift) % 26
            decrypted_message += UPPERCASE[new_index]
        # check if char is lowercase
        elif char.islower():
            index: int = LOWERCASE.index(char)
            new_index: int = (index - shift) % 26
            decrypted_message += LOWERCASE[new_index]
    return decrypted_message


def get_input() -> str:
    while True:
        try:
            # asks for a direction (encode or decode)
            direction: str = input("Encode or decode ( e or d): ").lower()
            match direction:
                case "e":
                    # asks for message and shift and inputs into encode function
                    message: str = input("Message: ")
                    shift: int = int(input("Shift: "))
                    result: str = encode(message, shift)
                    break
                case "d":
                    # asks for message and shift and inputs into decode function
                    message: str = str(input("Message: "))
                    shift: int = int(input("Shift: "))
                    result: str = decode(message, shift)
                    break
                case _:
                    raise ValueError
        except ValueError:
            print("[!] Incorrect value entered...")
    return result

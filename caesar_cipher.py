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

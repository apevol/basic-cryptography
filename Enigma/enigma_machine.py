# Define the rotor settings for the Enigma machine
rotor1: str = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2: str = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3: str = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector: str = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

# Define the starting position for each rotor
rotor1_start: int = 0
rotor2_start: int = 0
rotor3_start: int = 0

# Define the plugboard mapping which can be changed
plugboard = {"A": "B", "C": "D", "E": "F", "G": "H", "I": "J", "K": "L", "M": "N", "O": "P", "Q": "R", "S": "T",
             "U": "V", "W": "X", "Y": "Z"}


# run the enigma encoder
def run_enigma(msg: str) -> str:
    # grab global variables to use within function
    global rotor1_start, rotor2_start, rotor3_start
    msg = msg.upper()  # convert all to uppercase
    msg = msg.replace(" ", "")  # remove any whitespace

    encrypted_msg: list[str] = []  # define empty array for encrypted text

    # iterate over every character in input msg
    for char in msg:
        # apply plugboard
        char = plugboard.get(char, char)
        # increment start pos of rotor1
        rotor1_start = (rotor1_start + 1) % 26

        # check if first rotor has made a full revolution
        if rotor1_start == 0:
            rotor2_start = (rotor2_start + 1) % 26  # increment second rotor if so

            # check if second rotor has made a full revolution
            if rotor2_start == 0:
                rotor3_start = (rotor3_start + 1) % 26

        # map current character through all the rotors
        char = rotor1[(ord(char) - 65 + rotor1_start) % 26]
        char = rotor2[(ord(char) - 65 + rotor2_start) % 26]
        char = rotor3[(ord(char) - 65 + rotor3_start) % 26]

        # then map through reflector
        char = reflector[(ord(char) - 65) % 26]

        # Map the current character back through the all the in reverse
        char = chr((rotor3.index(char) - rotor3_start + 26) % 26 + 65)
        char = chr((rotor2.index(char) - rotor2_start + 26) % 26 + 65)
        char = chr((rotor1.index(char) - rotor1_start + 26) % 26 + 65)

        # map final msg through plugboard once again
        char = plugboard.get(char, char)

        # add the encrypted character to the encrypted message
        encrypted_msg.append(char)

    # join the encrypted message array into a single string
    encrypted_msg_str = "".join(encrypted_msg)

    return encrypted_msg_str  # return the encrypted value

# test
if __name__ == "__main__":
    encryption = run_enigma(msg="alan turing")
    print(f"Encrypted message is: {encryption}")

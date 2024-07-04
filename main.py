import caesar_cipher as caesar
import morse_code as morse


# gets input to define which cryptography method they would like to use
def get_mode() -> str:
    print("Current cryptography methods:" +
          "\nCaesar cipher (enter caesar to select)" +
          "\nMorse Code    (enter morse to select\n")
    while True:
        # gets user input and matches it to one of our cryptography methods
        mode: str = input("Enter cryptography method to use: ")
        match mode:
            case "caesar":
                result: str = caesar.get_input()
                return result
            case "morse":
                result: str = morse.get_input()
                return result
            case _:
                print("[!] Incorrect input entered...")


if __name__ == "__main__":
    result = get_mode()
    print(f"Result: {result}")

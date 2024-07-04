import caesar_cipher


# gets input to define which cryptography method they would like to use
def get_mode() -> str:
    print("Current cryptography methods:" +
          "\ncaesar cipher (enter caesar to select)")
    while True:
        # gets user input and matches it to one of our cryptography methods
        mode: str = input("Enter cryptography method to use: ")
        match mode:
            case "caesar":
                result: str = caesar_cipher.get_input()
                return result
            case _:
                print("[!] Incorrect input entered...")


if __name__ == "__main__":
    result = get_mode()
    print(f"Result: {result}")

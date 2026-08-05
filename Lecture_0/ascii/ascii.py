def check_ascii_code(char):
    if type(char) == str:
        print(ord(char))
    else:
        print("Please only enter a valid character on the ASCII Table")  

def check_character_type(char: str):
    if ord(char) >= 65 and ord(char) <= 90:
        print("Uppercase")
    elif ord(char) >= 97 and ord(char) <= 122:
        print("Lowercase")
    elif ord(char) >= 49 and ord(char) <= 57:
        print("Digit")
    else:
        print("Special Character")

character = input("Enter one character: ")
check_ascii_code(character)
check_character_type(character)

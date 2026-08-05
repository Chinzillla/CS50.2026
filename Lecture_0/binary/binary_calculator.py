number = int(input("Enter a number between 0 and 255 inclusive: "))
binary = ""

if 0 <= number <= 255:
    for i in range(7,-1,-1):
        if 2**i <= number:
            number -= 2**i
            binary += "1"
        else:
            binary += "0"
    print("The binary result is:", binary)
else:
    print("Please enter a valid number between 0 and 255")
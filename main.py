stored = 0


def encode(password):
    global stored
    result = ""
    for char in str(password):
        result += str((int(char) + 3))
    stored = int(result)

def decode(encoded_password):
    global stored
    encoded_password = str(stored)
    password = ''
    for digit in encoded_password:
        decoded_digit = (int(digit) - 3) % 10
        password += str(decoded_digit)
    return password


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            pass
        elif option == 3:
            #print(stored)
            break
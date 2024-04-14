def decode (passC):
    #already should be an integer at this point
    decoded = []
    for i in range (len(passC)):
        meow = passC[i] - 3
        decoded.append(meow)
    return decoded 


def encode_password(password):
    # Add your encoding logic here
    encoded_password = password[::-1]  # For demonstration purposes, simply reverse the password
    return encoded_password


def decode_password(encoded_password):
    # Add your decoding logic here
    decoded_password = encoded_password[::-1]  # For demonstration purposes, simply reverse the encoded password
    return decoded_password


def main():
    stored_password = None

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
            stored_password = encoded_password

        elif option == '2':
            if stored_password:
                print(
                    f"The encoded password is {stored_password}, and the original password is {decode_password(stored_password)}.")
            else:
                print("No password has been encoded yet. Please encode a password first.")

        elif option == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please enter a valid option.")


if __name__ == "__main__":
    main()

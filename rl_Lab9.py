def encode_password(password):
    encoded_password = " "
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode_password(encoded_password):
    decoded_password = " "
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

while True:
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = input("\nPlease enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = encode_password(password)
        print("Your password has been encoded and stored!")
    elif choice == "2":
        if 'encoded_password' in locals():
            print(f"The encoded password is {encoded_password}, and the original password is {decode_password(encoded_password)}.")
        else:
            print("You haven't encoded any password yet.")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please enter a valid option.")
